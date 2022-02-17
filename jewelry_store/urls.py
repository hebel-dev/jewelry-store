from django.urls import path

from . import views

app_name = 'jewelry_store'

urlpatterns = [
    path('', views.AllListView.as_view(), name='all_products'),
    
]
