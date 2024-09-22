from django import forms
from accounts.models import User

class CustomerSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_customer = True  # Définit is_customer à True
        if commit:
            user.save()
        return user
