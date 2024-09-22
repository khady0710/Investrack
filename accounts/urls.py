from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Connexion
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # Déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Inscription pour les clients (Customers)
    path('signup/', views.signup, name='signup'),

    # Redirection après connexion
    path('redirect/', views.user_redirect, name='user_redirect'),
]
