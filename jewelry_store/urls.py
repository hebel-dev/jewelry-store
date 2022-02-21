from django.urls import path

from . import views

app_name = 'jewelry_store'

urlpatterns = [
    path('', views.AllListView.as_view(), name='all_products'),
    path('product/<slug:slug>/', views.ProductView.as_view(), name='product_detail')
    
]
