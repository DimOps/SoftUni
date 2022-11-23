from product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters: float):
        super(Beverage, self).__init__(name, price)
        self.milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        if type(value) == float:
            self.__milliliters = value
        else:
            raise Exception('Milliliters must be float number')
