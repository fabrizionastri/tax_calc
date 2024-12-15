from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price_excl_tax = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)  

    @property
    def price_incl_tax(self):
        return round(self.price_excl_tax * (1 + self.tax_rate / 100), 2) 

    def __str__(self):
        return self.name
