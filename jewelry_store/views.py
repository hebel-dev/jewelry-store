from multiprocessing import context
from pyexpat import model
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
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
        
class ProductView(DetailView):
    context_object_name = 'product_detail'
    model = Product
    template_name = "jewelry_store/product/detail_product.html"

    # it shows 404 when object is not in stock 
    def get_object(self):
        obj = super().get_object()
        obj = get_object_or_404(Product, slug=self.kwargs['slug'] ,in_stock=True)
        return obj

