import requests
from .exceptions import *

URL = "https://open.neis.go.kr/hub/mealServiceDietInfo"


def get_meal_data(key, atpt_ofcdc_sc_code, sd_schul_code, mmeal_sc_code=None, mlsv_ymd=None,
                  mlsv_from_ymd=None, mlsv_to_ymd=None, pindex: int = 1, psize: int = 100):
    """
    신청주소: https://open.neis.go.kr/hub/mealServiceDietInfo
    신청제한횟수: 제한없음
    :param key:인증키
    :param atpt_ofcdc_sc_code:시도교육청코드
    :param sd_schul_code:표준학교코드
    :param mmeal_sc_code:식사코드
    :param mlsv_ymd:급식일자
    :param mlsv_from_ymd:급식시작일자
    :param mlsv_to_ymd: 급식종료일자
    :param pindex:페이지 위치
    :param psize:페이지 당 신청 숫자
    :return:급식
    """

    params = {
        "KEY": key,
        "Type": "json",
        "pIndex": pindex,
        "pSize": psize,
        "ATPT_OFCDC_SC_CODE": atpt_ofcdc_sc_code,
        "SD_SCHUL_CODE": sd_schul_code,
        "MMEAL_SC_CODE": mmeal_sc_code,
        "MLSV_YMD": mlsv_ymd,
        "MLSV_FROM_YMD": mlsv_from_ymd,
        "MLSV_TO_YMD": mlsv_to_ymd
    }

    res = requests.get(url=URL, params=params, verify=False, json=True)
    res.encoding = "UTF-8"
    request_json = res.json()

    try:
        status_code = request_json["mealServiceDietInfo"][0]["head"][1]["RESULT"]["CODE"]
    except KeyError:
        status_code = request_json["RESULT"]["CODE"]

    if status_code == "ERROR-300":
        raise IncorrectParamError()
    elif status_code == "ERROR-290":
        raise InvalidKeyError()
    elif status_code == "INFO-200":
        raise DataNotFoundError()

    meals = [SchoolMeal(data) for data in request_json["mealServiceDietInfo"][1]["row"]]

    return meals


class SchoolMeal:
    def __init__(self, meal_data):
        self.data = meal_data

    @property
    def region_code(self):
        return self.data["ATPT_OFCDC_SC_CODE"]

    @property
    def region(self):
        return self.data["ATPT_OFCDC_SC_NM"]

    @property
    def school_code(self):
        return self.data["SD_SCHUL_CODE"]

    @property
    def school(self):
        return self.data["SCHUL_NM"]

    @property
    def name(self):
        return self.data["MMEAL_SC_NM"]

    @property
    def date(self):
        return self.data["MLSV_YMD"]

    @property
    def meal(self):
        return self.data["DDISH_NM"].replace("<br/>", "\n")

    @property
    def origin(self):
        return self.data["ORPLC_INFO"].replace("<br/>", "\n")

    @property
    def calorie(self):
        return float(self.data["CAL_INFO"].split()[0])

    @property
    def nutrition(self):
        return self.data["NTR_INFO"].replace("<br/>", "\n")
