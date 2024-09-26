from django.urls import path
from . import views

urlpatterns = [
    # Tableau de bord des managers
    path('dashboard', views.manager_dashboard, name='manager_dashboard'),
    
    # Gestion des clients par les managers (si besoin)
    #path('customers/', views.manager_customer_list, name='manager_customer_list'),

    # Autres fonctionnalités des managers...
]
