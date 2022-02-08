from django.shortcuts import render

import jewelry_store

from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'jewelry_store/home.html', {'products':products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }