from django.contrib import admin

# Register your models here.
from customers.models import User


admin.site.register(User)