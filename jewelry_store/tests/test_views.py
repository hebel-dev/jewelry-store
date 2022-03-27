from audioop import reverse
from email.policy import default
from msilib.schema import ListView
from multiprocessing.connection import Client
from unittest import skip
from urllib import request, response

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from jewelry_store.models import Category, Collection, Product
from jewelry_store.views import AllListView

# @skip("demonstrating_skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()
        Category.objects.create(name='ring', slug='ring')
        Collection.objects.create(name='akacja', slug='akacja')
        User.objects.create(username='admin')
        self.data_prod = Product.objects.create(
           category_id = 1, 
           created_by_id = 1, #User(id=1),
           name = 'Gniot',
           model_number = 'Gniot/01/01/2022',
           material = default,
           purity = '.888',
           weight = '3.33',
           dimension = '223mmx12mmx4mm',
           image = 'gniot.JPG',
           price = '750.25',
           promo_price = '23.23',
           slug='Gniot',
           in_stock = 'True',
           not_new = 'True',
           size = '15/US8',
           created = '2022-01-31 15:01:26.543212',
           updated = '2022-01-31 15:01:27.123456'
       )

    def test_url(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code,200)

    
    def test_product_detail_url(self):
        response=self.c.get(reverse("jewelry_store:product_detail", args=['Gniot']))
        self.assertEqual(response.status_code,200) 

    def test_category_detail_url(self):
        response=self.c.get(reverse("jewelry_store:all_categories", args=['ring']))
        self.assertEqual(response.status_code,200)

    def test_collection_detail_url(self):
        response=self.c.get(reverse("jewelry_store:all_collections", args=['akacja']))
        self.assertEqual(response.status_code,200)

    def test_home_page_html(self):
        request = HttpRequest()
        response = request(AllListView)
        # print(response)