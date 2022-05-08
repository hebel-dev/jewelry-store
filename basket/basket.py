


from decimal import Decimal
from tkinter import YView
from jewelry_store.models import Product


class Basket():

    def __init__(self, request):
        # if sesion dosent exist the session will be created
        #every sesion is request
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def add(self,product, size, qty):
        product_id = product.id
        qty = 0
        if product_id is not self.basket:
            qty+=1
            self.basket[product_id] = {
                'price' : str(product.price), 
                'size': str(size),#from BasketAdd
                'qty' : int(qty),
                }
        
        self.session.modified = True
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database and return products
        
        """
        """ id's products in session """
        product_ids = self.basket.keys()
        """ compare produsts from db with products from session """
        products = Product.products.filter(id__in=product_ids)
        """ copy instance of session data """
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
            
        print('PRODUCT', basket)
        # print(basket.values())
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            print("ITEM1",item)
            item['total_price'] = item['price'] * item['qty']
            print("ITEM2",item)
            yield item 
        print(basket)    
    def __len__(self):
        """
        get the basket data and count the qty of items
       """

        return sum(item['qty'] for item in self.basket.values())