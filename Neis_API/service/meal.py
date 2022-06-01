from Neis_API.service.request import get_request

from Neis_API.service.exceptions import MealNotFoundError
from Neis_API.service.exceptions import UnknownMealCodeError

__SERVICE_NAME__ = "mealServiceDietInfo"
__URL__ = "https://open.neis.go.kr/hub/mealServiceDietInfo"


def _get_meals(region, school_code, meal_code=None, date=None, start_date=None, end_date=None, key=None, index: int = 1,
               size: int = 100):
    params = {
        "KEY": key,
        "Type": "json",
        "pIndex": index,
        "pSize": size,
        "ATPT_OFCDC_SC_CODE": region,
        "SD_SCHUL_CODE": school_code,
        "MMEAL_SC_CODE": meal_code,
        "MLSV_YMD": date,
        "MLSV_FROM_YMD": start_date,
        "MLSV_TO_YMD": end_date
    }

    return get_request(url=__URL__, service_name=__SERVICE_NAME__, params=params)


class MealInfo:
    def __init__(self, meal):
        pass


class Meal:
    _region_code: str
    _school_code: str

    _breakfast: MealInfo
    _lunch: MealInfo
    _dinner: MealInfo

    def __init__(self, meals: list):
        # if meals length is 0 -> raise error
        if not meals:
            raise MealNotFoundError()
        else:
            meal = meals[0]
            self._region_code = meal['ATPT_OFCDC_SC_CODE']
            self._school_code = meal['SD_SCHUL_CODE']

        for meal in meals:
            meal_info = MealInfo(meal)

            meal_code = meal["MMEAL_SC_CODE"]
            if meal_code == 1:
                self._breakfast = meal_info
            elif meal_code == 2:
                self._lunch = meal_info
            elif meal_code == 3:
                self._dinner = meal_info
            else:
                raise UnknownMealCodeError(meal_code=meal_code)

    @classmethod
    def meal_date(cls, region, school_code, date):
        resp = _get_meals(region=region, school_code=school_code, date=date)
        return Meal(resp)

    @property
    def region_code(self):
        return self._region_code

    @property
    def school_code(self):
        return self._school_code

    @property
    def breakfast(self):
        return self._breakfast

    @property
    def lunch(self):
        return self._lunch

    @property
    def dinner(self):
        return self._dinner

    def get_school(self):
        return
