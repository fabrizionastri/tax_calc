from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_excl_tax', 'tax_rate')