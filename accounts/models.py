from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser): 

    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

# Ajouter un related_name unique pour éviter les conflits
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Nom unique pour la relation inverse
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Nom unique pour la relation inverse
        blank=True,
    )