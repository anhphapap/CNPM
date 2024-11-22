import math
from models import Category, Product, User
from __init__ import app
import hashlib


def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, kw=None, page=None):
    prods = Product.query
    
    if kw:
        prods = prods.filter(Product.name.contains(kw))

    if cate_id:
        prods = prods.filter(Product.category_id == cate_id)

    if page:
        page_size = app.config["PRODUCTS_ON_PAGE"]
        pages = math.ceil(get_nums_product()/page_size)

    return prods.all()


def get_nums_product():
    return Product.query.count()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)