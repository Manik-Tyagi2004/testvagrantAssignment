
from shopping_apis import *

def test_app1() ->None:
    user = createUser(name="Manik1", phone_no="6396086643", is_admin = True)
    addProductToShop(user, createProduct(product_name="Leather Wallet", price=1100, gst=18, quantity = 10))
    addProductToShop(user, createProduct(product_name="Umbrella", price=900, gst=12, quantity = 10))
    addProductToShop(user, createProduct(product_name="Cigarette", price=200, gst=28, quantity = 10))
    addProductToShop(user, createProduct(product_name="Honey", price=100, gst=0, quantity = 10))
    

def test_app2() -> None:
    user = createUser(name="Manik2", phone_no = "6396078854")
    cart = createCart(user=user)
    addProductToCart(cart, getProductByName(product_name = "Leather Wallet" ), quantity=1)
    addProductToCart(cart, getProductByName(product_name = "Umbrella" ), quantity=2)
    addProductToCart(cart, getProductByName(product_name = "Cigarette" ), quantity=3)
    addProductToCart(cart, getProductByName(product_name = "Honey" ), quantity=4)
    showBill(cart)


    