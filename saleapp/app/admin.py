from __init__ import app, db
from models import User, Category, Product, UserRole
from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import redirect
import dao

admin = Admin(app=app, name='Sale', template_mode='bootstrap4')


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)


class CategoryView(AdminView):
    column_list = ['name', 'products']


class ProductView(AdminView):
    column_filters = ['price']
    column_list = ['name', 'category_id']
    can_export = True


class Authenticated(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(Authenticated):
    @expose('/')
    def index(self):
        logout_user()
        return redirect("/admin")


class StatsView(Authenticated):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html', stats=dao.revenue_stats())


admin.add_view(AdminView(User, db.session))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name="Thống kê"))
admin.add_view(LogoutView(name="Đăng xuất"))


