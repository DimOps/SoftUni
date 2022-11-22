from object_oriented_programming.inheritance.shop.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, quantity=10)


