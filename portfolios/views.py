from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioForm
from django.contrib.auth.decorators import login_required
from investments.models import Investment

# Liste des portefeuilles (Read)
@login_required
def portfolio_list(request):
    p_list = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolios/portfolio_list.html', {'portfolios': p_list})


# Détails d'un portefeuille (Read)
@login_required
def portfolio_detail(request, portfolio_id):
    p_show = get_object_or_404(Portfolio, id=portfolio_id)
    investments = Investment.objects.filter(portfolio=p_show)

    # Passer à la fois le portefeuille et les investissements au template
    context = {
        'portfolio': p_show,
        'investments': investments,
    }
    
    return render(request, 'portfolios/portfolio_detail.html', context)
   

# Création d'un portefeuille (Create)
@login_required
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            p_create = form.save(commit=False)
            p_create.user = request.user
            p_create.save()
            return redirect('p-list')
    else:
        form = PortfolioForm()
    return render(request, 'portfolios/portfolio_form.html', {'form': form})

# Mise à jour d'un portefeuille (Update)
@login_required
def portfolio_update(request, portfolio_id):
    p_update = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=p_update)
        if form.is_valid():
            form.save()
            return redirect('p-list')
    else:
        form = PortfolioForm(instance=p_update)
    return render(request, 'portfolios/portfolio_form.html', {'form': form})

# Suppression d'un portefeuille (Delete)
@login_required
def portfolio_delete(request, portfolio_id):
    p_delete = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        p_delete.delete()
        return redirect('portfolio_list')
    return render(request, 'portfolios/portfolio_confirm_delete.html', {'portfolio': p_delete})
