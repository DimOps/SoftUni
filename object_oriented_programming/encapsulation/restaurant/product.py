class Product:
    def __init__(self, name: str, price: float):
        self.price = price
        self.name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if type(value) == float:
            self.__price = value
        else:
            raise Exception('Price must be float')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
        else:
            raise Exception('Name must be string')