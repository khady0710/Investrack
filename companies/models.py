from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)  # Nom de l'entreprise
    sector = models.CharField(max_length=255)  # Secteur d'activité
    description = models.TextField()  # Description de l'entreprise

    # Quantité d'actions et obligations de l'entreprise
    total_shares = models.PositiveIntegerField(default=0)  # Nombre total d'actions
    total_bonds = models.PositiveIntegerField(default=0)  # Nombre total d'obligations

    # Prix d'achat des actions et obligations
    avg_share_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Prix moyen d'achat d'une action
    avg_bond_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Prix moyen d'achat d'une obligation

    def __str__(self):
        return self.name

    # Méthode pour calculer la valeur totale des actions
    def total_share_value(self):
        return self.total_shares * self.avg_share_price

    # Méthode pour calculer la valeur totale des obligations
    def total_bond_value(self):
        return self.total_bonds * self.avg_bond_price
