import cloudinary.uploader
from models import Category, Product, User
from __init__ import app, db
import hashlib
import cloudinary


def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, kw=None, page=1):
    prods = Product.query
    
    if kw:
        prods = prods.filter(Product.name.contains(kw))

    if cate_id:
        prods = prods.filter(Product.category_id == cate_id)

    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    prods = prods.slice(start, start + page_size)

    return prods.all()


def get_nums_product(cate_id=None, kw=None, page=1):
    prods = Product.query
    
    if kw:
        prods = prods.filter(Product.name.contains(kw))

    if cate_id:
        prods = prods.filter(Product.category_id == cate_id)

    return prods.count()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def add_user(name, username, password, avatar=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password)
    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res.get('secure_url')
    db.session.add(u)
    db.session.commit()