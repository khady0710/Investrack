from django.contrib import admin

# Register your models here.
from investments.models import Investment


admin.site.register(Investment)