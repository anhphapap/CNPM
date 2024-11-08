from flask import render_template
import dao
from app import app
from flask import request

@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get("category")
    kw = request.args.get('kw')
    prods = dao.load_products(cate_id, kw)
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)