from django.conf import settings

from product.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p) # iterate per product
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values()) # checking quantity in cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product.id, 'price': str(product.price)}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
            
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        
        self.save()

    def remove(self, product_id):
        if product_id not in self.cart:
            del self.cart[product_id]
            self.save()