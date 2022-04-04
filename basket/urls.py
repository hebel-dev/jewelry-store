from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [
    path('', views.BasketSummary.as_view(), name='basket_summary')
]
 