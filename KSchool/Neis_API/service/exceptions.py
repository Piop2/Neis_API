# service.meal
class UnknownMealCodeError(Exception):
    def __init__(self, meal_code):
        super().__init__("Unknown meal code error: %s" % meal_code)
        return
