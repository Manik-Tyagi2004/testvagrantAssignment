from user import User 
from product import Product

class Cart:
    
    def __init__(self, user):
        self.user = user 
        self.products = list[Product]

    def addProduct(self, product):
        self.products.append(product)

    def getProducts(self):
        return self.products
    
    

