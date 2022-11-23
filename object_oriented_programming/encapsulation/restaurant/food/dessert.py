from food.food import Food


class Desert(Food):
    def __init__(self, name, price, grams, calories: float):
        super(Desert, self).__init__(name, price, grams)
        self.calories = calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        if type(value) == float:
            self.__calories = value
        else:
            raise Exception('Calories must be float number')
