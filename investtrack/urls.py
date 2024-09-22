"""
URL configuration for investtrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL de l'admin de Django
    path('admin/', admin.site.urls),

    # Authentification : Connexion et Déconnexion
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Redirection après la connexion
    path('accounts/redirect/', include('accounts.urls')),  # Inclut la redirection et d'autres vues de l'app accounts

    # Inscription pour les clients
    path('accounts/signup/', include('accounts.urls')),

    # URLs spécifiques aux Managers
    path('managers/', include('managers.urls')),  # Gestion des fonctionnalités de l'application managers

    # URLs spécifiques aux Clients
    path('customers/', include('customers.urls')),  # Gestion des fonctionnalités de l'application customers

    # URLs pour les Portefeuilles
    path('portfolios/', include('portfolios.urls')),  # Gestion des portefeuilles

    # URLs pour les Investissements
    path('investments/', include('investments.urls')),  # Gestion des investissements

    # URLs pour les Entreprises
    path('companies/', include('companies.urls')),  # Gestion des entreprises

    # URLs pour les Documents Financiers
    path('financialdocuments/', include('financialdocuments.urls')),  # Gestion des documents financiers
]
