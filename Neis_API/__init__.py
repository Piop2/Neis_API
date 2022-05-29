import urllib3
from Neis_API.region import *
import Neis_API.service
# import Neis_API.school

urllib3.disable_warnings()

# service
info = service.info
meal = service.meal
schedule = service.schedule

# School = Neis_API.school.School

del urllib3, Neis_API
