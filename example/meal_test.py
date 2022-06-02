import Neis_API

data = Neis_API.Meal.meal_date(region=Neis_API.R_SEOUL, school_code="7010083", date="20220602")
print(data.dinner.dishs)
print(data.school_name)
