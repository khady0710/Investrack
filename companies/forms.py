from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'sector', 'description']  # Champs pour créer ou mettre à jour une entreprise
