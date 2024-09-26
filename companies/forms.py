from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'sector', 'description','total_shares','total_bonds','avg_share_price','avg_bond_price']  # Champs pour créer ou mettre à jour une entreprise
