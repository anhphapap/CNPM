from flask import render_template, request, redirect, jsonify, session
import dao
import utils
import math
from __init__ import app, login_manager
from flask_login import login_user, logout_user
from models import UserRole


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

            next = request.args.get('next')
            return redirect(next if next else '/')
        else:
            err_msg = "Password or username incorrect !!!"
    return render_template("login.html", err=err_msg)


@app.route("/admin-login", methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    u = dao.auth_user(username=username, password=password, role=UserRole.ADMIN)
    if u:
        login_user(u)
    return redirect("/admin")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/register", methods=['get', 'post'])
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
    return render_template("register.html", err=err_msg)


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/api/add-cart', methods=['post'])
def add_to_cart():
    id = str(request.json.get('id'))
    name = request.json.get('name')
    price = request.json.get('price')

    cart = session.get('cart')

    if not cart:
        cart = {}

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1
        }

    session['cart'] = cart
    print(utils.cal_cart(cart))
    return jsonify(utils.cal_cart(cart))


@app.route("/api/carts/<product_id>", methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')

    if cart and product_id in cart:
        quantity = int(request.json.get('quantity', 0))
        cart[product_id]['quantity'] = quantity

    session['cart'] = cart

    return jsonify(utils.cal_cart(cart))


@app.route('/api/carts/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')

    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.cal_cart(cart))


@app.route('/api/pay', methods=['post'])
def pay():
    try:
        dao.add_receipt(session.get('cart'))
    except:
        return jsonify({'status': 500})
    else:
        del session['cart']
        return jsonify({'status': 200})


@app.context_processor
def common_context_param():
    return {
        'categories': dao.load_categories(),
        'cart_stats': utils.cal_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from admin import admin
    app.run(debug=True)
