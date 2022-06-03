from Neis_API.service.request import get_request

__SERVICE_NAME__ = "mealServiceDietInfo"
__URL__ = "https://open.neis.go.kr/hub/mealServiceDietInfo"


def _get_meals(region=None, school_code=None, meal_code=None, date=None, start_date=None, end_date=None, key=None,
               index: int = 1,
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
    _type: str
    _population: str
    _dish: str
    _origin: str
    _calory: str
    _nutrition: str

    _exist: bool = False

    def __init__(self, meal):
        # self.meal = meal

        if meal:
            self._exist = True

            self._type = meal['MMEAL_SC_NM']  # 식사 종류
            self._population = meal['MLSV_FGR']  # 급식 인원 수
            self._dish = meal['DDISH_NM']  # 식단
            self._origin = meal['ORPLC_INFO']  # 원산지
            self._calory = meal['CAL_INFO']  # 칼로리
            self._nutrition = meal['NTR_INFO']  # 영양정보

    def is_exist(self):
        return self._exist

    @property
    def dish(self) -> list:
        return self._dish.split("\n")

    @property
    def dishs(self) -> str:
        return self._dish

    @property
    def type(self):
        return self._type

    @property
    def population(self):
        return self._population

    @property
    def origin(self):
        return self._origin.split("\n")

    @property
    def origins(self):
        return self._origin

    @property
    def calory(self):
        return self._calory.split("\n")

    @property
    def calorys(self):
        return self._calory

    @property
    def nutrition(self):
        return self._nutrition.split("\n")

    @property
    def nutritions(self):
        return self._nutrition


class Meal:
    _region_code: str
    _school_code: str
    _school_name: str
    _date: str

    _exist: bool

    _breakfast: MealInfo
    _lunch: MealInfo
    _dinner: MealInfo

    def __init__(self, meals: list):
        # self.meals = meals

        self._exist = False
        self._breakfast = MealInfo({})
        self._lunch = MealInfo({})
        self._dinner = MealInfo({})

        if len(meals):
            self._exist = True

            meal = meals[0]
            self._region_code = meal['ATPT_OFCDC_SC_CODE']
            self._school_code = meal['SD_SCHUL_CODE']
            self._school_name = meal['SCHUL_NM']
            self._date = meal['MLSV_YMD']

            for meal in meals:
                meal_info = MealInfo(meal)

                meal_code = meal['MMEAL_SC_CODE']
                if meal_code == "1":
                    self._breakfast = meal_info
                elif meal_code == "2":
                    self._lunch = meal_info
                elif meal_code == "3":
                    self._dinner = meal_info

    @classmethod
    def meal_date(cls, region: str, school_code: str, date: str):
        resp = _get_meals(region=region, school_code=school_code, date=date)
        return cls(resp)

    @classmethod
    def meal_daterange(cls, region: str, school_code: str, start: str, end: str):
        resp = _get_meals(region=region, school_code=school_code, start_date=start, end_date=end)

        # date of meal: MLSV_YMD

        meal_date: dict[str:list[dict]] = {}
        for r in resp:
            date = r['MLSV_YMD']
            if date in meal_date:
                meal_date[date].append(r)
            else:
                meal_date[date] = []

        meals = list(map(lambda x: Meal(x), meal_date.values()))
        return meals

    def is_exist(self):
        """오늘이 급식일 인가?"""
        return self._exist

    def get_school(self):
        return

    @property
    def region_code(self):
        return self._region_code

    @property
    def school_code(self):
        return self._school_code

    @property
    def school_name(self):
        return self._school_name

    @property
    def date(self):
        return self._date

    @property
    def breakfast(self):
        return self._breakfast

    @property
    def lunch(self):
        return self._lunch

    @property
    def dinner(self):
        return self._dinner
