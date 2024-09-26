from django.urls import path
from customers.views import customer_list,customer_detail,customer_create,customer_delete,customer_update


urlpatterns = [
    path("index", customer_list, name='cus-list'),
    path("show/<int:id>", customer_detail, name="cus-show"),
    path("create", customer_create, name='cus-create'),
    path("update/<int:id>", customer_update, name='cus-update'),
    path("delete/<int:id>", customer_delete, name='cus-delete'),
]