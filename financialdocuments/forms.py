from django import forms
from .models import FinancialDocument

class FinancialDocumentForm(forms.ModelForm):
    class Meta:
        model = FinancialDocument
        fields = ['company', 'document']  # Champs à afficher dans le formulaire
