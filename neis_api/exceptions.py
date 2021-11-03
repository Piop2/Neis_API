class Error300(Exception):
    def __init__(self):
        super().__init__("필수 값이 누락되어 있습니다. 요청인자를 참고 하십시오.")

class Error290(Exception):
    def __init__(self):
        super().__init__("인증키가 유효하지 않습니다. 인증키가 없는 경우, 홈페이지에서 인증키를 신청하십시오.")

class Info200(Exception):
    def __init__(self):
        super().__init__("해당하는 데이터가 없습니다.")
