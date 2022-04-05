import urllib3

urllib3.disable_warnings()

from .region import *

import Neis_API.service

get_meal = Neis_API.service.schoolMeal.get_meal_data
get_school = Neis_API.service.schoolInfo.get_school_data
get_schedule = Neis_API.service.schoolschedule.get_schedule_data

import Neis_API.school

School = Neis_API.School
