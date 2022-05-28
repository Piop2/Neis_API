from Neis_API.service.request import get_request

__SERVICE_NAME__ = "mealServiceDietInfo"
__URL__ = "https://open.neis.go.kr/hub/mealServiceDietInfo"


def get_meal(region, school_code, meal_code=None, date=None, start_date=None, end_date=None, key=None, index: int = 1,
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


def date_meal(region, school_code, *date):
    start_date = None
    end_date = None

    if len(date) == 1:
        start_date = date[0]
        end_date = date[0]
    elif len(date) == 2:
        start_date = date[0]
        end_date = date[1]
    else:
        print("Hi, I am ERROR")

    return get_meal(region=region, school_code=school_code, start_date=start_date, end_date=end_date)


class SchoolMeal:
    pass


class Breakfast:
    pass


class Lunch:
    pass


class Dinner:
    pass
