from ast import mod
from decimal import Decimal
from random import choice, choices
from tabnanny import verbose
from traceback import print_exception
from unicodedata import category, name
from django.db import models
from django.forms import DecimalField
from django.contrib.auth.models import User

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
    (_5 , "5/ø14mm/US4"),
    (_6 , "6/ø14.3mm/US4+"),
    (_7 , "7/ø14.6mm/"),
    (_8 , "8/ø15mm/US5"),
    (_9 , "9/ø15.3mm"),
    (_10, "10/ø15.6mm/US6-"),
    (_11, "11/ø16mm/US6"),
    (_12, "12/ø16.3mm"),
    (_13, "13/ø16.6mm"),
    (_14, "14/ø17mm/US7"),
    (_15, "15/ø17.3mm"),
    (_16, "16/ø17.6mm/US7+"),
    (_17, "17/ø18mm/US8"),
    (_18, "18/ø18.3mm"),
    (_19, "19/ø18.6mm/US9"),
    (_20, "20/ø19mm"),
    (_21, "21/ø19.3mm/US9+"),
    (_22, "22/ø19.6mm/US10"),
    (_23, "23/ø20mm"),
    (_24, "24/ø20.3mm/US11-"),
    (_25, "25/ø20.6mm/US11"),
    (_26, "26/ø21mm"),
    (_27, "27/ø21.3/US12"),
    (_28, "28/ø21.6"),
    (_29, "29/ø22mm/US13-"),
    (_30, "30/ø22.3mm/US13"),
    (_31, "31/ø22.6mm"),
    (_32, "32/ø23mm/US14"),
    (_33, "33/ø23.3mm"),
    (_34, "34/ø23.6mm"),
 ]

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=50)
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, default="silver")
    purity = models.CharField(max_length=4, choices=PURITY_CHOICES,default=".925")
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimension = models.CharField(max_length=255)  ###!!!
    image = models.ImageField(upload_to = 'images/') ###!!! only one option
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    not_new = models.BooleanField(default=True)
    size = models.CharField(max_length=17, choices=SIZE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural = 'Products'
        ordering = ('-created','-updated','weight', 'price',) 

    def __str__(self):
        return self.name