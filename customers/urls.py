from django.urls import path
from customers.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='cus-list'),
    path("show/<int:id>", show, name="cus-show"),
    path("create/", create, name='cus-create'),
    path("update/<int:id>", update, name='cus-update'),
    path("delete/<int:id>", delete, name='cus-delete'),
]