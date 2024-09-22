from django.urls import path
from investments.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='i-list'),
    path("show/<int:id>", show, name="i-show"),
    path("create/", create, name='i-create'),
    path("update/<int:id>", update, name='i-update'),
    path("delete/<int:id>", delete, name='i-delete'),
]