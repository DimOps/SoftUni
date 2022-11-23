from product import Product


class Food(Product):
    def __init__(self, name, price, grams: float):
        super(Food, self).__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        if type(value) == float:
            self.__grams = value
        else:
            raise Exception('Grams must be float number')