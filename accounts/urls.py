from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.user_redirect, name='user_redirect'),  # Vue de redirection
    #path('signup/', views.signup, name='signup'),  # Exemple d'une page d'inscription
]
