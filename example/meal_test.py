import KSchool

meals = Neis_API.meal.meal_date(region=Neis_API.R_SEOUL, school_code="7010083", date="20220610")
for meal in meals:
    print(f"----{meal.type}----")
    print(meal.dishs)
