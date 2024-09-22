from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required

# Liste des clients (Read)
@login_required
def customer_list(request):
    cus_list = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': cus_list})

# Détails d'un client (Read)
@login_required
def customer_detail(request, customer_id):
    cus_show = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': cus_show})

# Création d'un client (Create)
@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cus-list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

# Mise à jour d'un client (Update)
@login_required
def customer_update(request, customer_id):
    cus_update = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=cus_update)
        if form.is_valid():
            form.save()
            return redirect('cus-list')
    else:
        form = CustomerForm(instance=cus_update)
    return render(request, 'customers/customer_form.html', {'form': form})

# Suppression d'un client (Delete)
@login_required
def customer_delete(request, customer_id):
    cus_delete = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        cus_delete.delete()
        return redirect('cus-list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': cus_delete})
