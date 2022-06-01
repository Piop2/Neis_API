# service.meal
class MealNotFoundError(Exception):
    def __init__(self):
        super().__init__("There is no meal today")


class UnknownMealCodeError(Exception):
    def __init__(self, meal_code):
        super().__init__("Unknown meal code error: %s" % meal_code)
        return
