from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_redirect(request):
    if request.user.is_manager:
        return redirect('manager_dashboard')  # Redirige vers le tableau de bord du manager
    elif request.user.is_customer:
        return redirect('customer_dashboard')  # Redirige vers le tableau de bord du client
    else:
        return redirect('default_dashboard')  # Redirige vers un tableau de bord par défaut
