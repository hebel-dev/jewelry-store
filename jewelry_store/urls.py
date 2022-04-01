from unicodedata import name

from django.urls import path

from jewelry_store.models import Category

from . import views

app_name = 'jewelry_store'

urlpatterns = [
    path('', views.AllListView.as_view(), name='all_products'),
    path('<slug:slug>', views.ProductView.as_view(), name='product_detail'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='all_categories'),
    path('collection/<slug:slug>/', views.CollectionView.as_view(), name='all_collections'),
    
]
 