from django.db import models
from accounts.models import User
from django.conf import settings
# Create your models here.

class Customer(models.Model):

    firstname = models.CharField(max_length=30) # name VARCHAR(30) NOT NULL
    lastname = models.CharField(max_length=30) # name VARCHAR(30) NOT NULL
    email = models.EmailField(max_length=30) # name VARCHAR(30) NOT NULL
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, null=True, blank=True)
    job = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"