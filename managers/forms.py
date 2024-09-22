from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['firstname','lastname']  # Champs spécifiques au Manager
