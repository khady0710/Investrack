from django.shortcuts import render, get_object_or_404, redirect
from .models import FinancialDocument
from .forms import FinancialDocumentForm
from django.contrib.auth.decorators import login_required

# Liste des documents financiers (Read)
@login_required
def document_list(request):
    f_list = FinancialDocument.objects.all()
    return render(request, 'financialdocuments/document_list.html', {'documents': f_list})

# Détails d'un document financier spécifique (Read)
@login_required
def document_detail(request, document_id):
    f_show = get_object_or_404(FinancialDocument, id=document_id)
    return render(request, 'financialdocuments/document_detail.html', {'document': f_show})

# Création d'un nouveau document financier (Create)
@login_required
def document_create(request):
    if request.method == 'POST':
        form = FinancialDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('f-list')
    else:
        form = FinancialDocumentForm()
    return render(request, 'financialdocuments/document_form.html', {'form': form})

# Mise à jour d'un document financier existant (Update)
@login_required
def document_update(request, document_id):
    f_update = get_object_or_404(FinancialDocument, id=document_id)
    if request.method == 'POST':
        form = FinancialDocumentForm(request.POST, request.FILES, instance=f_update)
        if form.is_valid():
            form.save()
            return redirect('f-list')
    else:
        form = FinancialDocumentForm(instance=f_update)
    return render(request, 'financialdocuments/document_form.html', {'form': form})

# Suppression d'un document financier (Delete)
@login_required
def document_delete(request, document_id):
    f_delete = get_object_or_404(FinancialDocument, id=document_id)
    if request.method == 'POST':
        f_delete.delete()
        return redirect('f-list')
    return render(request, 'financialdocuments/document_confirm_delete.html', {'document': f_delete})
