from django.urls import path
from managers.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='m-list'),
    path("show/<int:id>", show, name="m-show"),
    path("create/", create, name='m-create'),
    path("update/<int:id>", update, name='m-update'),
    path("delete/<int:id>", delete, name='m-delete'),
]