from django.urls import path
from companies.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='c-list'),
    path("show/<int:id>", show, name="c-show"),
    path("create/", create, name='c-create'),
    path("update/<int:id>", update, name='c-update'),
    path("delete/<int:id>", delete, name='c-delete'),
]