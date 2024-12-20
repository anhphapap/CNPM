import cloudinary.uploader
from models import Category, Product, User, ReceiptDetails, Receipt
from __init__ import app, db
import hashlib
import cloudinary
from flask_login import current_user
from sqlalchemy import func


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


def auth_user(username, password, role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User.query.filter(User.username.__eq__(username), User.password.__eq__(password))
    if role:
        u = u.filter(User.user_role.__eq__(role))
    return u.first()


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


def add_receipt(cart):
    if cart:
        r = Receipt(user=current_user)
        db.session.add(r)

        for c in cart.values():
            d = ReceiptDetails(quantity=c['quantity'], unit_price=c['price'],
                               receipt=r, product_id=c['id'])
            db.session.add(d)

        db.session.commit()


def revenue_stats():
    return db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.quantity * ReceiptDetails.unit_price))\
                     .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id)).group_by(Product.id).all()