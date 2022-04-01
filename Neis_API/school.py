from .service.mealInfo import get_meal_data
from .service.schoolInfo import get_school_data
from .service.schoolschedule import get_schedule_data


class School:
    def __init__(self, school_data, key=None):
        self.key = key

        self.school_data = school_data

    def __str__(self):
        return self.name

    @property
    def region_code(self):
        return self.school_data.region_code

    @property
    def region(self):
        return self.school_data.region_name

    @property
    def code(self):
        return self.school_data.school_code

    @property
    def name(self):
        return self.school_data.school_name

    @classmethod
    def find(cls, region_code, school_code, key=None):
        """
        지역코드와 학교코드로 학교를 찾고 School객체를 리합니다.
        :param region_code: 지역코드
        :param school_code: 학교코드
        :param key: API 인증키
        :return: class School
        """
        school_data = get_school_data(region_code=region_code,
                                      school_code=school_code,
                                      key=key)[0]
        return School(school_data=school_data)

    def get_meal_info(self, start_date=None, end_date=None, pindex: int = 1, psize: int = 100):
        """
        :param start_date:급식시작일자 또는 급식일자
        :param end_date: 급식종료일자
        :param pindex:페이지 위치
        :param psize:페이지 당 신청 숫자
        :return:검색된 모든 급식
        """

        date = None

        if start_date is None:
            raise TypeError("'NoneType' object cannot be a start_date")

        if end_date is None:
            date = start_date
            start_date = None

        return get_meal_data(
            region_code=self.region_code,
            school_code=self.code,
            date=date,
            start_date=start_date,
            end_date=end_date,
            key=self.key,
            pindex=pindex,
            psize=psize
        )

    def get_school_info(self):
        return self.school_data

    def get_schedule_info(self, dght_crse_sc_nm=None, schul_crse_sc_nm=None, date=None, start_date=None, end_date=None, pindex: int = 1, psize: int = 100):
        """
        :param dght_crse_sc_nm: 주야과정명
        :param schul_crse_sc_nm: 학교과정명
        :param date: 학사일자
        :param start_date: 학사시작일자
        :param end_date: 학사종료일자
        :param pindex: 페이지 위치
        :param psize: 페이지 당 신청 숫자 (필수)
        :return: 검색된 모든 학교 (필수)
        """
        return get_schedule_data(
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
