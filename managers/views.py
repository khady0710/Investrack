from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def manager_dashboard(request):
    if not request.user.is_manager:
        return HttpResponse('Accès refusé')  # Vérification que l'utilisateur est bien un manager
    return render(request, 'managers/dashboard.html')
