from __future__ import annotations

import collections
from ast import arg, mod
from asyncio.windows_events import NULL
from decimal import Decimal
from email.policy import default
from itertools import product
from pickle import EMPTY_DICT, TRUE
from queue import Empty
from random import choice, choices
from tabnanny import verbose
from traceback import print_exception
from unicodedata import category, name

import pkg_resources
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Sum
from django.forms import DecimalField
from django.urls import reverse
from multiselectfield import MultiSelectField

Au = "gold"
Ag = "silver"
AuWoo = "wood&gold"
AgWoo = "wood&silver"
MATERIAL_CHOICES = [
    (Au, "gold"),
    (Ag,"silver"),
    (AuWoo, "wood&gold"),
    (AgWoo, "wood&silver"),
]

_999 = ".999"
_925 = ".925"
_875 = ".875"
_830 = ".830"
_800 = ".800"
_960 = ".960"
_750 = ".750"
_585 = ".585"
_500 = ".500"
_375 = ".375"
_333 = ".333"
PURITY_CHOICES =[
    (_999, ".999"),(_925, ".925"),(_875, ".875"),(_830, ".830"),
    (_800, ".800"),(_960, ".960"),(_750, ".750"),(_585, ".585"),
    (_500, ".500"),(_375, ".375"),(_333, ".333"),
]
_5  = "5/ø14mm/US4"
_6  = "6/ø14.3mm/US4+"
_7  = "7/ø14.6mm/"
_8  = "8/ø15mm/US5"
_9  = "9/ø15.3mm"
_10 = "10/ø15.6mm/US6-"
_11 = "11/ø16mm/US6"
_12 = "12/ø16.3mm"
_13 = "13/ø16.6mm"
_14 = "14/ø17mm/US7"
_15 = "15/ø17.3mm"
_16 = "16/ø17.6mm/US7+"
_17 = "17/ø18mm/US8"
_18 = "18/ø18.3mm"
_19 = "19/ø18.6mm/US9"
_20 = "20/ø19mm"
_21 = "21/ø19.3mm/US9+"
_22 = "22/ø19.6mm/US10"
_23 = "23/ø20mm"
_24 = "24/ø20.3mm/US11-"
_25 = "25/ø20.6mm/US11"
_26 = "26/ø21mm"
_27 = "27/ø21.3/US12"
_28 = "28/ø21.6"
_29 = "29/ø22mm/US13-"
_30 = "30/ø22.3mm/US13"
_31 = "31/ø22.6mm"
_32 = "32/ø23mm/US14"
_33 = "33/ø23.3mm"
_34 = "34/ø23.6mm"
SIZE_CHOICES  =  [
    (_5 , "5/ø14mm/US4"), (_6 , "6/ø14.3mm/US4+"), (_7 , "7/ø14.6mm/"),
    (_8 , "8/ø15mm/US5"),(_9 , "9/ø15.3mm"), (_10, "10/ø15.6mm/US6-"),
    (_11, "11/ø16mm/US6"), (_12, "12/ø16.3mm"), (_13, "13/ø16.6mm"),
    (_14, "14/ø17mm/US7"), (_15, "15/ø17.3mm"), (_16, "16/ø17.6mm/US7+"),
    (_17, "17/ø18mm/US8"), (_18, "18/ø18.3mm"), (_19, "19/ø18.6mm/US9"),
    (_20, "20/ø19mm"), (_21, "21/ø19.3mm/US9+"), (_22, "22/ø19.6mm/US10"),
    (_23, "23/ø20mm"), (_24, "24/ø20.3mm/US11-"), (_25, "25/ø20.6mm/US11"),
    (_26, "26/ø21mm"), (_27, "27/ø21.3/US12"), (_28, "28/ø21.6"),
    (_29, "29/ø22mm/US13-"), (_30, "30/ø22.3mm/US13"), (_31, "31/ø22.6mm"),
    (_32, "32/ø23mm/US14"), (_33, "33/ø23.3mm"), (_34, "34/ø23.6mm"),
 ]
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True,in_stock=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("jewelry_store:all_categories", args=[self.slug])
    
    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Collections'
    
    def get_absolute_url(self):
        return reverse("jewelry_store:all_collections", args=[self.slug])

    def __str__(self):
        return self.name

    @property
    def price(self):
        price = 0
        for product in self.products.all():
            price += product.price
        return price    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    colection_name = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=50)
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, default="silver")
    purity = models.CharField(max_length=4, choices=PURITY_CHOICES,default=".925")
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimension = models.CharField(max_length=255)  ###!!!
    image = models.ImageField(upload_to = 'images/', default='images/default.jpg') ###!!! only one option
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    not_new = models.BooleanField(default=True)
    size = MultiSelectField(choices=SIZE_CHOICES,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = ProductManager()

    @property
    def quantity(self):
        quantity = 0
        if not self.size:
            quantity = 1
        else:
            store = len(self.size)
            quantity += store
        return quantity



    class Meta():
        verbose_name_plural = 'Products'
        ordering = ('-created','-updated','weight', 'price',) 

    def get_absolute_url(self):
        return reverse("jewelry_store:product_detail", args=[self.slug])
    #def collection_sumarum(self):#    v=Product.objects.filter(price=True).aggregate(Sum('price'))#    print(v)# collections=Product.objects.get(pk=colection_name_id).aggregate(Sum('price'))# key_collections = Collection.id.#collections = Product.objects.filter(colection_name_id=1)#print('COLLECTIONS',collections)# for product in collections:#     Decimal(product.price)#     price = []#     a=type(Decimal(product.price))#     # print(a)#     # print(price)#     price.append(Decimal(product.price))# print(price)# print('FIRST',product.price)# print("ŁołołO",price)# v=Product.objects.aggregate(Sum('price')){{ p.collection_sumarum }}# print(collections)# return print('COLLECTIONS',collections)

    # def sum_total(self) :
    #     queryset = Product.objects.filter(in_stock=True)
    #     collections = Collection.objects.all()
    #     sum_tot=0
    #     for col in collections:
    #         for qs in queryset:
    #             if qs.colection_name_id == col.id:
    #                 sum_tot += qs.price
    #                 print('sum_tot',sum_tot)
    #     # queryset = sum_tot
    #     # print("bbbbbb",queryset)    
    #     return sum_tot

    def sum_total(self) :
        queryset = Product.objects.filter(in_stock=True)
        collections = Collection.objects.all()
        sum_tot=0
        for col in collections:
            for qs in queryset:
                if qs.colection_name_id == col.id:
                    sum_tot += qs.price
                    print('sum_tot',sum_tot)
        # queryset = sum_tot
        # print("bbbbbb",queryset)    
    def sum_total(self) :
        queryset = Product.products.filter(in_stock=True)
        collections = Collection.objects.all()
        sum_tot=0
        sum_tot_list = []
        num = len(collections)
        print('numer dlugosci listy',num)
        for col in collections:
            print(col.id)
            print(collections)    
                
            
            for qs in queryset:
                # for col.id in collections:
                    # print("col.id", col.id)
                if col.id ==  qs.colection_name_id:
                   
                    sum_tot += qs.price
                    
                    
                    print('sum_tot',sum_tot)
                    sum_tot_list.append(sum_tot)
        # queryset = sum_tot
        # print("bbbbbb",queryset)    
            return sum_tot

    def __str__(self):
        return self.name


# python manage.py makemigrations and python manage.py migrate

        