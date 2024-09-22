from django.shortcuts import render, get_object_or_404, redirect
from .models import Investment
from .forms import InvestmentForm
from django.contrib.auth.decorators import login_required

# Liste des investissements (Read)
@login_required
def investment_list(request, portfolio_id):
    i_list = Investment.objects.filter(portfolio__id=portfolio_id)
    return render(request, 'investments/investment_list.html', {'investments': i_list})

# Détails d'un investissement (Read)
@login_required
def investment_detail(request, investment_id):
    i_show = get_object_or_404(Investment, id=investment_id)
    return render(request, 'investments/investment_detail.html', {'investment': i_show})

# Création d'un investissement (Create)
@login_required
def investment_create(request, portfolio_id):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            i_create = form.save(commit=False)
            i_create.portfolio_id = portfolio_id
            i_create.save()
            return redirect('i-list', portfolio_id=portfolio_id)
    else:
        form = InvestmentForm()
    return render(request, 'investments/investment_form.html', {'form': form})

# Mise à jour d'un investissement (Update)
@login_required
def investment_update(request, investment_id):
    i_update = get_object_or_404(Investment, id=investment_id)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=i_update)
        if form.is_valid():
            form.save()
            return redirect('i-list', portfolio_id=i_update.portfolio.id)
    else:
        form = InvestmentForm(instance=i_update)
    return render(request, 'investments/investment_form.html', {'form': form})

# Suppression d'un investissement (Delete)
@login_required
def investment_delete(request, investment_id):
    i_delete = get_object_or_404(Investment, id=investment_id)
    if request.method == 'POST':
        i_delete.delete()
        return redirect('i-list', portfolio_id=i_delete.portfolio.id)
    return render(request, 'investments/investment_confirm_delete.html', {'investment': i_delete})
