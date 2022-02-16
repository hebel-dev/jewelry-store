from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views import generic

import jewelry_store

from .models import Category, Product

# def all_products(request):
#     products = Product.objects.all()
#     return render(request, 'jewelry_store/home.html', {'products':products})

# zamiast robię aktualnie templatetags
# def categories(request):
    
#     return {
#         'categories': Category.objects.all()
#     }

class ProductListView(generic.ListView):
    model = Product
    template_name = 'jewelry_store/home.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #         context[""] = 
    #         return context
        
