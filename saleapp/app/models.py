from __init__ import app, db
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as RoleEnum
from flask_login import UserMixin


class UserRole(RoleEnum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg")
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    product = relationship("Product", backref="category", lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # import hashlib
        # pwd = str(hashlib.md5("123456".encode('utf-8').strip()).hexdigest())
        # u = User(name='admin',  username='admin', password=pwd, user_role=UserRole.USER)
        # db.session.add(u)
        # db.session.commit()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        # products = [{
        #     "id": 7,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 8,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 9,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # },
        #     {
        #         "id": 10,
        #         "name": "iPhone 7 Plus",
        #         "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #         "price": 17000000,
        #         "image":
        #             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #         "category_id": 1
        #     }, {
        #         "id": 11,
        #         "name": "iPad Pro 2020",
        #         "description": "Apple, 128GB, RAM: 6GB",
        #         "price": 37000000,
        #         "image":
        #             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #         "category_id": 2
        #     }, {
        #         "id": 12,
        #         "name": "Galaxy Note 10 Plus",
        #         "description": "Samsung, 64GB, RAML: 6GB",
        #         "price": 24000000,
        #         "image":
        #             "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #         "category_id": 1
        #     }
        # ]
        #
        # for p in products:
        #     db.session.add(Product(**p))
        # db.session.commit()

