import collections
from gettext import Catalog
from multiprocessing import context

from django.db.models import Sum
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import DetailView, ListView
from pyexpat import model

import jewelry_store

from .models import Category, Collection, Product


class AllListView(ListView):
    context_object_name = 'all_products'
    queryset = Product.products.filter(in_stock=True, is_active = True)
    template_name = 'jewelry_store/home.html'
    # pk_url_kwarg='collection_id' 
    
    def get_context_data(self, **kwargs,):
        
        context = super(AllListView,self).get_context_data(**kwargs)
           
        print('dupaaaa',kwargs)
        # print(context)
        context['collections'] =  Collection.objects.all
        context['products'] = self.queryset
        
        context['sum']= Product.products.all()
        
        print("DUPA1",Product.products.filter(colection_name=1))
        print("DUPA2",Product.products.filter(colection_name=self.kwargs.get('collection_id')))
        context['prodo'] = Product.products.all().aggregate(Sum('price'))['price__sum']
        print("context['prodo']",context['prodo'])

        return context
        
    def get_queryset(self) :
        queryset = Product.products.filter(in_stock=True, is_active=True)
        collections = Collection.objects.all()
        sum_tot=0
        for col in collections:
            for qs in queryset:
                if qs.colection_name_id == col.id:
                    sum_tot += qs.price
                    print('sum_tot',sum_tot)
        queryset = sum_tot
        print("aaaaaa",queryset)    
        return queryset


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
        products = Product.products.filter(category__slug=self.kwargs['slug'],in_stock=True, is_active=True)
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
    pk_url_kwarg = 'collection_id'
    
    def get_queryset(self):
        products = Product.products.filter(colection_name__slug=self.kwargs['slug'],in_stock=True, is_active=True)
        # the same but shorter, was down # category = get_object_or_404(Category,slug=self.kwargs['slug'])# print(category)# products = Product.objects.filter(category=category)# print(products)
        return products    #Product.objects.filter(category=category)#products#Product.objects.filter(category=category)#products#
    
    def get_context_data(self,**kwargs):
        context = super(CollectionView,self).get_context_data(**kwargs)
        context['collection'] = get_object_or_404(Collection,slug=self.kwargs['slug'])
        products = Product.products.filter(colection_name__slug=self.kwargs['slug'])
        context['prodo'] = products.aggregate(Sum('price'))
        return context
