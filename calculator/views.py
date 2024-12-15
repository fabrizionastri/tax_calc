from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse ,HttpResponse
from .models import Product 

def index(request):
    products = Product.objects.all()
    return render(request, 'calculator.html', {'products': products}) 

def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_update.html', {'product': product})

def create_product(request):     
    if request.method == 'POST': 
        name = request.POST['product_name']
        price_excl_tax = float(request.POST['price_excl_tax']) 
        tax_rate = float(request.POST['tax_rate'])
        product = Product.objects.create(
            name=name,
            price_excl_tax=price_excl_tax,
            tax_rate=tax_rate ,
        )  
    return render(request, 'product_row.html', {'product': product})

def delete_product(request, pk): 
    product = get_object_or_404(Product, pk=pk)
    product.delete() 
    return HttpResponse('')  

def update_product(request):  
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST': 
        product.name = request.POST['product_name']
        product.price_excl_tax = float(request.POST['price_excl_tax'])
        product.tax_rate = float(request.POST['tax_rate'])
        product.save()

    return render(request, 'product_row.html', {'product': product})        
