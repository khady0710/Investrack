from django import forms
from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['company', 'investment_type', 'quantity', 'purchase_price', 'purchase_date']  # Champs nécessaires pour l'investissement
