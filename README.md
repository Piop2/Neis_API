# Neis API

[![PyPI version](https://badge.fury.io/py/Neis-API.svg)](https://badge.fury.io/py/Neis-API)<a href="https://pypi.org/project/Neis-API"><img src="https://img.shields.io/pypi/dm/Neis-API" alt="PyPI downloads"></a>

Neis_API를 사용하기 위해서는 토큰이 필요합니다.<br/>
토큰은 [나이스 교육정보 개방 포탈](https://open.neis.go.kr/portal/mainPage.do) 에서 신청할 수 있습니다.

## 특징

- 나이스 API에 올라와있는 데이터를 가져오고, 활용할 수 있습니다.

## 설치

```shell
pip install Neis-API
```

## 예제
### Region
```python
# API에서 필수로 입력되어야 하는 시도교육청코드입니다.
from Neis-API import Region
# SEOUL     (서울) : B10
# BUSAN     (부산) : C10
# DAEGU     (대구) : D10
# INCHEON   (인천) : E10
# GWANGJU   (광주) : F10
# DAEJEON   (대전) : G10
# ULSAN     (울산) : H10
# SEJONG    (세종) : I10
# GYEONGGI  (경기) : J10
# GANGWON   (강원) : K10
# CHUNGBUK  (전북) : M10
# CHUNGNAM  (전남) : N10
# JEONBUK   (전북) : P10
# JEONNAM   (전남) : Q10
# GYEONGBUK (경북) : R10
# GYEONGNAM (경남) : S10
# JEJU      (제주) : T10
# FORIENGER (그 외 국제학교) : V10

print(Region.SEOUL)

### 출력 ###
# B10
```

### mealInfo
```py
from Neis-API import Region, mealInfo

# 날짜로 급식찾기
data = mealInfo.get_meal_data(key= "토큰",
                              atpt_ofcdc_sc_code=Region.SEOUL,
                              sd_schul_code="7091432",
                              mlsv_ymd="20211109")
print(data[0].ddish_nm) # tuple형식으로 return됩니다(검색 정확도 순)

### 결과 ###
# 기장흑미밥
# 얼큰꽃게탕5.8.9.13.17.18.
# 감자채볶음1.5.10.13.
# 매콤닭불구이1.2.5.6.15.
# 배추김치9.13.
# 힘내파인애플씨13.
```

## 라이선스

이 프로젝트는 MIT License에 속해 있습니다.

## 도와주신 분

- [hyunwoo6321](https://github.com/hyunwoo6321)
