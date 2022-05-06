from itertools import product
from multiprocessing import context
from pyexpat import model
from re import template
from urllib import response
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

import basket
from jewelry_store.models import Product
from .basket import Basket
# Create your here.

class BasketSummary(View):
    # model = Product
    # template_name = 'jewelry_store/basket/summary.html'
    context_object_name = 'product_detail'

    def get(self, request, *args, **kwargs):
        basket = Basket(request)
        basketwxample= basket.__iter__()
        
        # print(basket)
        # form = self.form_class
        return render(request ,'jewelry_store/basket/summary.html',{'basket' : basket})
# class BasketAdd(ListView):
#     model = Basket

class BasketAddView(View):
    
    
    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))## if somethink like number is after colon , take post in insomnia and look at the print    
        product_size = str(request.POST.get('productsize'))#'productsize' from ajax data
        print('dupa',product_size)
        product_qty = str(request.POST.get('productqty'))
        print('dupa',product_qty)
            #get product from data base
        product = get_object_or_404(Product, id=product_id) #it was id and should be p
        #print(product)
        
        basket.add(product=product, size=product_size, qty = product_qty)
        basketqty=basket.__len__()
        
        # print('DUPA', basketqty)
        response = JsonResponse({'size': product_size,'product' : product_id, 'qty': basketqty, }) 
        return response

    
    # def get(self, request, *args, **kwargs):
    #     return response  

#####   wyci\agbiety product do funkcji

    # def post(self, request, *args, **kwargs):
    #     basket = Basket(request)
    #     product = self.get_product(request) #wyciągnięty product
    #     basket.add(product=product)
    #     response = JsonResponse({'test': 'data' })
    #     return response

    # def get_product(self, request):
    #     product_id = int(request.POST.get('product_id',1))## if somethink like number is after colon , take post in insomnia and look at the print    
    #     print('dupa',product_id)
    #         #get product from data base
    #     product = get_object_or_404(Product, id=product_id) #it was id and should be p
    #     #print(product)
    #     return product


    ### pierwsza wersja funkcyjna
    
# def basket_add(request):
#         #grab session data
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#             #create product id and data from ajax - value after click on button
#         product_id = int(request.POST.get('productid'))
#         print(product_id)
#             #get product from data base
#         product = get_object_or_404(Product, id=product_id) #it was id and should be p
#         # send data to basket(session)
#         basket.add(product=product)

#         response = JsonResponse({'test': 'data' })
#         return response
        