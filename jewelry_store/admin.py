
from django.contrib import admin

from .models import Category, Collection, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model_number','material','purity','weight','price', 'promo_price', 
    'slug', 'in_stock', 'not_new', 'created', 'updated', 'size']

    list_filter = ['material','purity','in_stock', 'size','not_new','category' ]
    list_editable = ['price', 'promo_price','in_stock' ]
    prepopulated_fields = {'slug':('name',)}

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}