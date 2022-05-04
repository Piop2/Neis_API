from urllib3 import disable_warnings
from Neis_API.region import *
import Neis_API.date
import Neis_API.service
import Neis_API.school

disable_warnings()

Date = Neis_API.date.Date

get_meal = Neis_API.service.schoolMeal.get_meal_data
get_school = Neis_API.service.schoolInfo.get_school_data
get_schedule = Neis_API.service.schoolSchedule.get_schedule_data

School = Neis_API.school.School
