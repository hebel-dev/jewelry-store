from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView

import jewelry_store

from .models import Category, Collection, Product

# def all_products(request):
#     products = Product.objects.all()
#     return render(request, 'jewelry_store/home.html', {'products':products})

# zamiast robię aktualnie templatetags
# def categories(request):
    
#     return {
#         'categories': Category.objects.all()
#     }

class AllListView(ListView):
    context_object_name = 'all_products'
    queryset = Product.objects.all
    template_name = 'jewelry_store/home.html'

    def get_context_data(self,**kwargs):
        context = super(AllListView,self).get_context_data(**kwargs)
        context['collections'] =  Collection.objects.all
        context['products'] = self.queryset
        return context
        
