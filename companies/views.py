from django.shortcuts import render, get_object_or_404, redirect
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required

# Liste des entreprises (Read)
def company_list(request):
    c_list = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': c_list})

# Détails d'une entreprise (Read)
def company_detail(request, company_id):
    c_show = get_object_or_404(Company, id=company_id)
    return render(request, 'companies/company_detail.html', {'company': c_show})

# Création d'une entreprise (Create)
@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('c-list')
    else:
        form = CompanyForm()
    return render(request, 'companies/company_form.html', {'form': form})

# Mise à jour d'une entreprise (Update)
@login_required
def company_update(request, company_id):
    c_update = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=c_update)
        if form.is_valid():
            form.save()
            return redirect('c-list')
    else:
        form = CompanyForm(instance=c_update)
    return render(request, 'companies/company_form.html', {'form': form})

# Suppression d'une entreprise (Delete)
@login_required
def company_delete(request, company_id):
    c_delete = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        c_delete.delete()
        return redirect('c-list')
    return render(request, 'companies/company_confirm_delete.html', {'company': c_delete})
