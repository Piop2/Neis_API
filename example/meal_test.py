import Neis_API

data = Neis_API.Meal.meal_date(Neis_API.R_SEOUL, "7010083", date="20220531")
print(data._data)