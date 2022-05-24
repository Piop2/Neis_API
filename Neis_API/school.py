from ast import Str
from Neis_API.service import school_meal, school_info, school_schedule
from Neis_API.region import region_name

from Neis_API.exceptions import *


class School:
    _region: str
    _code: str
    _key: str

    def __init__(self, *args, key: str = None):
        """
        School 객체를 지정하여 여러 정보를 불러옵니다
        :param args: (region, school_code), (SchoolMeal / SchoolInfo / Schedule)
        :param key: API KEY
        """
        self._region = None
        self._code = None
        self._key = key

        if len(args) == 2:
            self._region, self._code = args
        elif isinstance(args[0], schoolMeal.SchoolMeal) or isinstance(args[0], schoolInfo.SchoolInfo) or isinstance(
                args[0], schoolSchedule.SchoolSchedule):
            self._region = args[0].region_code
            self._code = args[0].school_code

    @property
    def region_code(self) -> str:
        return self._region

    @property
    def region_name(self) -> str:
        return region_name(self._region)

    @property
    def school_code(self) -> str:
        return self._code

    @staticmethod
    def find(region_code: str=None, school_code: str=None, school_name: str=None, key: str=None) -> School:
        """
        지역코드와 학교코드로 학교를 찾고 School객체를 리합니다.
        :param region_code: 지역코드
        :param school_code: 학교코드
        :param key: API 인증키
        :return: class School
        """
        school_data = schoolInfo.get_school_data(region_code=region_code,
                                                 school_code=school_code,
                                                 school_name=school_name,
                                                 key=key)[0]
        return School(school_data)

    def get_meal(self, *args, pindex: int = 1, psize: int = 100):
        """
        get meal_data with date range or date
        """

        start_date = None
        end_date = None

        if len(args) == 1:
            start_date = args[0]
            end_date = args[0]
        elif len(args) == 2:
            start_date = args[0]
            end_date = args[1]
        else:
            raise DateRangeError()

        return schoolMeal.get_meal_data(
            region=self.region_code,
            school_code=self.school_code,
            start_date=start_date,
            end_date=end_date,
            key=self._key,
            pindex=pindex,
            psize=psize
        )

    def get_school(self):
        return

    def get_schedule(self, dght_crse_sc_nm=None, schul_crse_sc_nm=None, date=None, start_date=None, end_date=None,
                     pindex: int = 1, psize: int = 100):
        return schoolSchedule.get_schedule_data(
            region_code=self.region_code,
            school_code=self.code,
            dght_crse_sc_nm=dght_crse_sc_nm,
            schul_crse_sc_nm=schul_crse_sc_nm,
            date=date,
            start_date=start_date,
            end_date=end_date,
            key=self.key,
            pindex=pindex,
            psize=psize
        )
