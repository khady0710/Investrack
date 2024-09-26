from django.urls import path
from financialdocuments.views import document_list, document_detail,document_create,document_update,document_delete

urlpatterns = [
    path("index", document_list, name='f-list'),
    path("show/<int:id>", document_detail, name="f-show"),
    path("create", document_delete, name='f-create'),
    path("update/<int:id>", document_update, name='f-update'),
    path("delete/<int:id>", document_delete, name='f-delete'),
]