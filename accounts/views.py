from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm

# Vue pour rediriger l'utilisateur après la connexion en fonction de son type
@login_required
def user_redirect(request):
    if request.user.is_manager:
        return redirect('manager_dashboard')  # Redirige vers le tableau de bord du manager
    elif request.user.is_customer:
        return redirect('customer_dashboard')  # Redirige vers le tableau de bord du client
    else:
        return redirect('default_dashboard')  # Tableau de bord par défaut

# Vue pour s'inscrire en tant que Customer
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True  # Définit l'utilisateur comme Customer
            user.save()
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})
