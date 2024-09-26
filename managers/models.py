from django.db import models

# Create your models here.

class Manager(models.Model):

    firstname = models.CharField(max_length=30) # name VARCHAR(30) NOT NULL
    lastname = models.CharField(max_length=30) # name VARCHAR(30) NOT NULL
    email = models.EmailField(max_length=30) # name VARCHAR(30) NOT NULL
    phone = models.CharField(max_length=30, null=True, blank=True)



    def __str__(self):
        return f"{self.firstname} {self.lastname}"