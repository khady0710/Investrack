from django.contrib import admin

# Register your models here.
from financialdocuments.models import FinancialDocument


admin.site.register(FinancialDocument)