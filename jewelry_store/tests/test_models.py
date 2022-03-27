from asyncio.windows_events import NULL
from email.policy import default
from os import name
from unicodedata import category

from django.contrib.auth.models import User
from django.test import TestCase

from jewelry_store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data_cat = Category.objects.create(name='ring', slug='ring')

    def test_category_model_entry(self):

        data = self.data_cat
        self.assertTrue(isinstance(data,Category)) 
    
    def test_category_model_entry(self):

        data=self.data_cat
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'ring')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='ring', slug='ring')
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
    def test_product_model_entry(self):
        data = self.data_prod
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data), 'Gniot')