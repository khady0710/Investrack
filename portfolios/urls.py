from django.urls import path
from portfolios.views import portfolio_list,portfolio_detail,portfolio_create,portfolio_update,portfolio_delete

urlpatterns = [
    path("customer_dashboard", portfolio_list, name='p-list'),
    path("show/<int:id>", portfolio_detail, name="p-show"),
    path("create", portfolio_create, name='p-create'),
    path("update/<int:id>", portfolio_update, name='p-update'),
    path("delete/<int:id>", portfolio_delete, name='p-delete'),
]