import Neis_API

meals = Neis_API.meal.meal_daterange(region=Neis_API.R_SEOUL, school_code="7010083", start="20220530", end="20220531")
for meal in meals:
    print(f"<{meal.date}급식>")
    print(meal.dinner.dishs)
    print()
