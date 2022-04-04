from django.views.generic import ListView
from django.shortcuts import render

import basket
from jewelry_store.models import Product

# Create your here.

class BasketSummary(ListView):
    model = Product
    template_name = "jewelry_store/basket/summary.html"
