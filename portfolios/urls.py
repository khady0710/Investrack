from django.urls import path
from portfolios.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='p-list'),
    path("show/<int:id>", show, name="p-show"),
    path("create/", create, name='p-create'),
    path("update/<int:id>", update, name='p-update'),
    path("delete/<int:id>", delete, name='p-delete'),
]