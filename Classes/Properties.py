# There are times that you want to have control over an attribute in class
# For example you have crated a product class and a constructor to set the price of the product
# but with this implementation self.price = price you can give a it a negative value

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            return ValueError("Price cannot be a negetive number.")
        self.__price = value


product = Product(-10)
print(product.price)

# A simple solution is to make price private (self.__price)
# and setting 2 methods for getting and setting the value
# Property: an object that sits in front of an attribute and allows us to get or set the value

# Now with the set price and get price properties available, this will fix our problem...but they are still accessbile
# when you type product. you will see get_price and set_price
# This polluting the interface of our object. Imagine having a remote with 50 buttons on it
# You want your objects to have minimal methods exposed to the outside

# To hide get_price and set_price you CAN make them private (__get_price, __set_price) but this adds extra noise to the code
# Instead use a decorator
