from food.dessert import Desert


class Cake(Desert):
    _GRAMS = 250
    _CALORIES = 1000
    _PRICE = 5

    def __init__(self, name):
        super(Cake, self).__init__(name,  Cake._PRICE, Cake._GRAMS, Cake._CALORIES)
