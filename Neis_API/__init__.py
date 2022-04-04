import urllib3
urllib3.disable_warnings()

from .region import *

from .service import *

get_meal= schoolMeal.get_meal_data
get_school = schoolInfo.get_school_data
get_schedule = schoolSchedule.get_schedule_data

from .school import *