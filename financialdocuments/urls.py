from django.urls import path
from financialdocuments.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='f-list'),
    path("show/<int:id>", show, name="f-show"),
    path("create/", create, name='c-create'),
    path("update/<int:id>", update, name='f-update'),
    path("delete/<int:id>", delete, name='f-delete'),
]