from Neis_API.service.request import get_request
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


class Meal:
    def __init__(self, meals):
        self._region_code = None
        self._school_code = None

        self._breakfast = None
        self._lunch = None
        self._dinner = None

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


class MealInfo:
    def __init__(self, meal):
        pass
