from gettext import Catalog
from multiprocessing import context
from pyexpat import model
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
import jewelry_store

from .models import Category, Collection, Product
from django.db.models import Sum

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

class CategoryView(ListView):
    model = Category
    context_object_name = 'all_categories'
    template_name = 'jewelry_store/product/category.html'

    def get_queryset(self):
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        # the same but shorter, was down # category = get_object_or_404(Category,slug=self.kwargs['slug'])# print(category)# products = Product.objects.filter(category=category)# print(products)
        return products    #Product.objects.filter(category=category)#products#Product.objects.filter(category=category)#products#
    
    def get_context_data(self,**kwargs):
        context = super(CategoryView,self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category,slug=self.kwargs['slug'])
        return context
class CollectionView(ListView):
    #  context_object_name = 'collection_detail'#  queryset = Product.objects.all#  template_name = "jewelry_store/product/detail_collection.html"#  def get_context_data(self,**kwargs):#     context = super(ListView,self).get_context_data(**kwargs)#     context['collections'] =  Collection.objects.all #     context['products'] = self.queryset#     return context
    model = Collection
    context_object_name = 'all_collections'
    template_name = 'jewelry_store/product/collections.html'

    def get_queryset(self):
        products = Product.objects.filter(colection_name__slug=self.kwargs['slug'])
        # the same but shorter, was down # category = get_object_or_404(Category,slug=self.kwargs['slug'])# print(category)# products = Product.objects.filter(category=category)# print(products)
        return products    #Product.objects.filter(category=category)#products#Product.objects.filter(category=category)#products#
    
    def get_context_data(self,**kwargs):
        context = super(CollectionView,self).get_context_data(**kwargs)
        context['collection'] = get_object_or_404(Collection,slug=self.kwargs['slug'])
        return context

    