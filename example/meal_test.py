import Neis_API

data = Neis_API.meal.meal_date(region=Neis_API.R_SEOUL, school_code="7010083", date="20220602")
print(data.breakfast.type)

