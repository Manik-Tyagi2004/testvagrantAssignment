from math import prod
from cart import Cart
from shop import Shop 
from user import User 
from product import Product

shop = Shop()

def createUser(name, phone_no) -> User:
    user = User(name, phone_no)
    return user 

def createCart(user: User):
    cart = Cart(user = user)
    return cart 

def createProduct(user, product_name, price, gst, quantity):
    product = Product(product_name, price, gst, quantity)
    return product

def addProductToShop(user, product):
    shop.addProduct(user, product)

def getProductByName(product_name):
    for product in shop.getProducts():
        if(product.getName() == product_name):
            return product 
    return None 

def addProductToCart(cart: Cart, product):
    cart.addProduct(product)

def showBill(cart):
    for product in cart.getProducts():
        print(product.getName(), shop.calculatePriceOfProduct(product))
    print("final Price: ", shop.calculatePriceOfCart(cart))
