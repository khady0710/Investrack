from django.db import models
from customers.models import Customer

class Portfolio(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Customer: {self.customer.user.username})"

    def total_investments(self):
        # Import local pour éviter les importations circulaires
        from investments.models import Investment
        return Investment.objects.filter(portfolio=self).count()

    def total_investment_amount(self):
        from investments.models import Investment
        investments = Investment.objects.filter(portfolio=self)
        total_amount = sum([inv.purchase_price * inv.quantity for inv in investments])
        return total_amount

    def investment_types(self):
        from investments.models import Investment
        investments = Investment.objects.filter(portfolio=self).values_list('investment_type', flat=True).distinct()
        return list(investments)

    def invested_companies(self):
        from investments.models import Investment
        investments = Investment.objects.filter(portfolio=self).values_list('company__name', flat=True).distinct()
        return list(investments)
