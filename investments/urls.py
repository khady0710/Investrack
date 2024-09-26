from django.urls import path
from investments.views import investment_list,investment_create,investment_detail,investment_update,investment_delete


urlpatterns = [
    path("index/<int:portfolio_id>/", investment_list, name='i-list'),  
    path("show/<int:id>", investment_detail, name="i-show"),
    path("create/", investment_create, name='i-create'),
    path("update/<int:id>", investment_update, name='i-update'),
    path("delete/<int:id>", investment_delete, name='i-delete'),
]