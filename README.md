<h1 style="text-align: center">Neis API</h1>

[![PyPI version](https://badge.fury.io/py/Neis-API.svg)](https://badge.fury.io/py/Neis-API)
<a href="https://pypi.org/project/Neis-API"><img src="https://img.shields.io/pypi/dm/Neis-API" alt="PyPI downloads"></a>
<a href="https://github.com/Piop2/Neis_API/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)" alt="./LICENSE"></a>

Neis API는 나이스 API를 활용할 수 있게 도와주는 패키지입니다.</br>
나이스 API에 대한 자세한 설명은 [나이스 교육 개방 포털](https://open.neis.go.kr/portal/mainPage.do)에서 보실 수 있습니다.

# 설치

### PYPI를 이용한 설치

아래 명령어로 간단하게 설치할 수 있습니다.

```commandline
pip install Neis-API
```

아래 명령어로 패키지를 업그레이드 할 수 있습니다

```commandline
pip install -U Neis-API
```

### github에서 설치

Neis_API레포의 release를 보면 .whl파일이 업로드 되어있습니다.

개발 버전은 acions의 artifacts에서 확인하실 수 있습니다.

이를 다운받아 아래의 명령어를 실행합니다.

```commandline
pip install [.whl 파일 경로 및 이름]
```

# 예제

### 급식 메뉴 받아오기(Neis_API)

```python
from KSchool import Neis_API


data = Neis_API.meal.meal_date(region=Neis_API.R_SEOUL, school_code="7010080", date="20220701")
print(data.lunch)
```

# 도움주신 분
- [hyunwoo6321](https://github.com/hyunwoo6321)
