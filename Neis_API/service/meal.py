from Neis_API.school import School

from Neis_API.service.request import get_request

from Neis_API.service.exceptions import UnknownMealCodeError

SERVICE_NAME = "mealServiceDietInfo"
URL = "https://open.neis.go.kr/hub/mealServiceDietInfo"


def _get_meals(region=None, school_code=None, meal_code=None, date=None, start_date=None, end_date=None, key=None,
               index: int = 1, size: int = 100):
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

    return get_request(url=URL, service_name=SERVICE_NAME, params=params)


def meal_date(region: str, school_code: str, date: str):
    resp = _get_meals(region=region, school_code=school_code, date=date)
    return Meal(resp)


def meal_daterange(region: str, school_code: str, start: str, end: str):
    resp = _get_meals(region=region, school_code=school_code, start_date=start, end_date=end)

    # date of meal: MLSV_YMD

    meal_dates: dict[str:list[dict]] = {}
    for r in resp:
        date = r['MLSV_YMD']
        if date in meal_dates:
            meal_dates[date].append(r)
        else:
            meal_dates[date] = []

    meals = {}
    for k, v in meal_dates.items():
        meals[k] = Meal(v)

    return Meals(meals=meals)


class MealInfo:
    _type: str
    _population: int
    _dish: str
    _origin: str
    _calory: str
    _nutrition: str

    _exist: bool = False

    def __init__(self, meal):
        # self.meal = meal
        self._c = 0

        if meal:
            self._exist = True

            self._type = meal['MMEAL_SC_NM']  # 식사 종류
            self._population = int(meal['MLSV_FGR'])  # 급식 인원 수
            self._dish = meal['DDISH_NM']  # 식단
            self._origin = meal['ORPLC_INFO']  # 원산지
            self._calory = meal['CAL_INFO']  # 칼로리
            self._nutrition = meal['NTR_INFO']  # 영양정보

    def __iter__(self):
        self._c = 0
        return self

    def __next__(self):
        if self._c < len(self.dish):
            dish = self.dish[self._c]
            self._c += 1
            return dish
        else:
            raise StopIteration

    def __str__(self):
        return self.dishs

    def is_exist(self):
        return self._exist

    @property
    def dish(self) -> list:
        try:
            return self._dish.split("\n")
        except AttributeError:
            return []

    @property
    def dishs(self) -> str:
        try:
            return self._dish
        except AttributeError:
            return ""

    @property
    def type(self) -> str:
        try:
            return self._type
        except AttributeError:
            return ""

    @property
    def population(self) -> int:
        try:
            return self._population
        except AttributeError:
            return 0

    @property
    def origin(self) -> list:
        try:
            return self._origin.split("\n")
        except AttributeError:
            return []

    @property
    def origins(self) -> str:
        try:
            return self._origin
        except AttributeError:
            return ""

    @property
    def calory(self) -> list:
        try:
            return self._calory.split("\n")
        except AttributeError:
            return []

    @property
    def calorys(self) -> str:
        try:
            return self._calory
        except AttributeError:
            return ""

    @property
    def nutrition(self) -> list:
        try:
            return self._nutrition.split("\n")
        except AttributeError:
            return []

    @property
    def nutritions(self) -> str:
        try:
            return self._nutrition
        except AttributeError:
            return ""


class Meals:
    _meals_date: dict
    _meals: list

    def __init__(self, meals):
        self._c = 0
        self._meals_date = meals
        self._meals = list(meals.values())

    def __iter__(self):
        self._c = 0
        return self

    def __next__(self):
        if self._c < len(self._meals_date):
            meal = self._meals[self._c]
            self._c += 1
            return meal
        else:
            raise StopIteration

    def __len__(self):
        return len(self._meals)

    def get_meal(self, date):
        if date in self._meals_date:
            return self._meals_date[date]
        return

    @property
    def meals(self):
        return self._meals


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
        # self._meals = meals

        self._c = 0

        self._exist = False
        self._breakfast = MealInfo({})
        self._lunch = MealInfo({})
        self._dinner = MealInfo({})

        if meals:
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
                else:
                    UnknownMealCodeError(meal_code=meal_code)

    def is_exist(self):
        """오늘이 급식일 인가?"""
        return self._exist

    def get_school(self):
        return School(region_code=self._region_code, school_code=self._school_code)

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

    def __len__(self):
        """존재하는 급식의 개수"""
        n = 0
        for meal in [self._breakfast, self._lunch, self._dinner]:
            if meal.is_exist():
                n += 1
        return n

    def __iter__(self):
        self._c = 0
        return self

    def __next__(self):
        meals = [self._breakfast, self._lunch, self._dinner]
        if self._c < len(meals):
            meal = meals[self._c]
            self._c += 1
            return meal
        else:
            raise StopIteration
