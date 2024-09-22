from django.db import models
from portfolios.models import Portfolio
from companies.models import Company

class Investment(models.Model):
    INVESTMENT_TYPES = [
        ('action', 'Action'),
        ('obligation', 'Obligation'),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)  # Portefeuille associé
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Entreprise associée
    investment_type = models.CharField(max_length=20, choices=INVESTMENT_TYPES)  # Type d'investissement
    quantity = models.PositiveIntegerField()  # Quantité d'actions ou obligations
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix d'achat
    purchase_date = models.DateField()  # Date d'achat

    def __str__(self):
        return f"{self.quantity} {self.get_investment_type_display()} in {self.company.name} (Portfolio: {self.portfolio.name})"
