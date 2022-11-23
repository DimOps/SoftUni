from beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    _MILLILITERS = 50
    _PRICE = 3.5

    def __init__(self, name, caffeine: float):
        super(Coffee, self).__init__(name, Coffee._PRICE, Coffee._MILLILITERS)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        if type(value) == float:
            self.__caffeine = value
        else:
            raise Exception('Caffeine must be float value')
