from models import Category, Product


def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, kw=None):
    prods = Product.query

    if kw:
        prods = prods.filter(Product.name.contains(kw))

    if cate_id:
        prods = prods.filter(Product.category_id == cate_id)
    return prods.all()
