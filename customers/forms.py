from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','email','address', 'phone']  # Champs que tu veux rendre modifiables pour un Customer
