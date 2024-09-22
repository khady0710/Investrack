from django.db import models
from companies.models import Company

class FinancialDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Entreprise associée
    document = models.FileField(upload_to='financial_documents/')  # Chemin du document uploadé
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Date de téléchargement

    def __str__(self):
        return f"Document for {self.company.name} uploaded on {self.uploaded_at}"
