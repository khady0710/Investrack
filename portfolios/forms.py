from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['customer','name','created_at','total_investments','total_investment_amount','investment_types','invested_companies']  # Le nom du portefeuille, par exemple
