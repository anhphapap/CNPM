from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user, logout_user


@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get("category")
    kw = request.args.get("kw")
    prods = dao.load_products(cate_id, kw)
    return render_template("index.html", categories=cates, products=prods)


@app.route("/login", methods=['get', 'post'])
def login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect("/")
    return render_template("login.html")


@login.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


# @app.route("/register")
# def register():
#     return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
