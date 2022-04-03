from .region import *

from .service.mealInfo import get_meal_data
from .service.schoolInfo import get_school_data
from .service.schoolschedule import get_schedule_data

from .school import School

import urllib3
urllib3.disable_warnings()