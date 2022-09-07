from product import Product

class Shop:
    
    def __inti__(self):
        self.products = list[Product]
    
    def addProduct(self, user, product):
        if(user.isAdmin()):
            self.products.append(product)

    def calculatePriceOfProduct(self, product):
        return product.getPrice() - self.calculateDiscount(product) - self.calculateGST(product);


    def calculateDiscount(product):
        
        pass 

    def calculateGST(product):
        pass
    
    def calculatePriceOfCart(self, cart):
        price = 0
        for product in cart.getProducts():
            price += (product.getPrice() - self.calculateDiscount(price) - self.calculateGST(product)) 
        return price 

    
