class Product:
    def __init__(self, product_name, price, gst, quantity):
        self.product_name = product_name
        self.price = price 
        self.gst = gst 
        self.quantity = quantity
    
    def getName(self):
        return self.product_name

