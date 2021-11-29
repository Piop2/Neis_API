# Neis API

[![PyPI version](https://badge.fury.io/py/Neis-API.svg)](https://badge.fury.io/py/Neis-API)<a href="https://pypi.org/project/Neis-API"><img src="https://img.shields.io/pypi/dm/Neis-API" alt="PyPI downloads"></a>

Neis_API는 나이스 교육정보 개방 포탈을 이용합니다.<br/>
자세한 정보는 [나이스 교육정보 개방 포탈](https://open.neis.go.kr/portal/mainPage.do) 를 참고해주세요.

## 특징

- 나이스 API에 올라와있는 데이터를 가져오고, 활용할 수 있습니다.

## 설치

```shell
pip install Neis-API
```

## 예시

### School
```python
from Neis_API import Region, School

school = School.find(region_code=Region.SEOUL,
                     school_name="서운중학교")
meal_data = school.get_meal_info(2021, 11, 9)
print(meal_data.ddish_nm)
### 출력 ###
# 기장흑미밥
# 얼큰꽃게탕5.8.9.13.17.18.
# 감자채볶음1.5.10.13.
# 매콤닭불구이1.2.5.6.15.
# 배추김치9.13.
# 힘내파인애플씨13.

school_data = school.get_school_info()
print(school_data.sd_schul_code)
### 출력 ###
# 7091432
```

### mealInfo
```python
# 날짜로 급식찾기
from Neis_API import Region, mealInfo

data = mealInfo.get_meal_data(atpt_ofcdc_sc_code=Region.SEOUL,
                              sd_schul_code="7091432",
                              mlsv_ymd="20211109")
print(data[0].ddish_nm)

### 출력 ###
# 기장흑미밥
# 얼큰꽃게탕5.8.9.13.17.18.
# 감자채볶음1.5.10.13.
# 매콤닭불구이1.2.5.6.15.
# 배추김치9.13.
# 힘내파인애플씨13.
```

### schoolInfo
```python
# 이름으로 학교 코드 찾기
from Neis_API import Region, schoolInfo

# 시도교육청코드는 필수 값이 아니지만 학교 검색의 정확도를 높이기 위해 넣었습니다.
school_name = "서운중학교"
data = schoolInfo.get_school_data(atpt_ofcdc_sc_code=Region.SEOUL,
                                  schul_nm=school_name)
print(data[0].sd_schul_code)
### 출력 ###
# 7091432
```

## 사용
### Region
```
Region.SEOUL     (서울) : B10
Region.BUSAN     (부산) : C10
Region.DAEGU     (대구) : D10
Region.INCHEON   (인천) : E10
Region.GWANGJU   (광주) : F10
Region.DAEJEON   (대전) : G10
Region.ULSAN     (울산) : H10
Region.SEJONG    (세종) : I10
Region.GYEONGGI  (경기) : J10
Region.GANGWON   (강원) : K10
Region.CHUNGBUK  (전북) : M10
Region.CHUNGNAM  (전남) : N10
Region.JEONBUK   (전북) : P10
Region.JEONNAM   (전남) : Q10
Region.GYEONGBUK (경북) : R10
Region.GYEONGNAM (경남) : S10
Region.JEJU      (제주) : T10
Region.FORIENGER (그 외 국제학교) : V10
```

## 오류 (exceptions)
```
ERROR-300   : 필수 값이 누락되어 있습니다... -> 필수값을 다시 확인해주십시오.
ERROR-290   : 인증키가 유효하지 않습니다... -> KEY값 오류입니다.
ERROR-333   : 요청위치 값의 타입이 유효하지 않습니다... -> pindex 또는 isize의 값이 자연수로 설정해주세요.
ERROR-336   : 데이터요청은 한번에 최대 1,000건을 넘을 수 없습니다.
ERROR-337   : 일별 트래픽 제한을 넘은 호출입니다. 오늘은 더이상 호출할 수 없습니다.
ERROR-500   : 서버 오류입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.
ERROR-600   : 데이터베이스 연결 오류입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.
ERROR-601   : SQL 문장 오류 입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.


INFO-300    : 관리자에 의해 인증키 사용이 제한되었습니다.
INFO-200    : 해당하는 데이터가 없습니다.
```

## 라이선스

이 프로젝트는 MIT License에 속해 있습니다.

## 도와주신 분

- [hyunwoo6321](https://github.com/hyunwoo6321)
