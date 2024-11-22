from flask import render_template, request, redirect
import dao
import math
from __init__ import app, login_manager
from flask_login import login_user, logout_user


@app.route("/")
def index():
    cate_id = request.args.get("category")
    kw = request.args.get("kw")
    if request.args.get("page"):
        page = int(request.args.get("page"))
    else:
        page = 1
    prods = dao.load_products(cate_id, kw, page)
    page_size = app.config["PAGE_SIZE"]
    pages = math.ceil(dao.get_nums_product(cate_id, kw, page)/page_size)
    return render_template("index.html", products=prods, pages=pages)


@app.route("/login", methods=['get', 'post'])
def login():
    err_msg = None
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect("/")
        else:
            err_msg = "Password or username incorrect !!!"
    return render_template("login.html", err=err_msg)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/register", methods=['get','post'])
def register():
    err_msg = None
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password.__eq__(confirm):
            data = request.form.copy()
            del data['confirm']

            avatar = request.files.get('avatar')
            if dao.add_user(avatar=avatar, **data):
                return redirect('/login')
            else:
                err_msg = 'Something is wrong please try again'
        else:
            err_msg = 'Password incorrect'
    return render_template("register.html", err = err_msg)


@app.context_processor
def common_context_param():
    return {
        'categories' : dao.load_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)
