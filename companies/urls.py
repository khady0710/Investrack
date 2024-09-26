from django.urls import path
from companies.views import company_list, company_detail,company_create,company_update,company_delete  


urlpatterns = [
    path("index", company_list, name="c-list"),
    path("show/<int:id>", company_detail, name="c-show"),
    path("create", company_create, name='c-create'),
    path("update/<int:id>", company_update, name='c-update'),
    path("delete/<int:id>", company_delete, name='c-delete'),
]