"""
SEOUL : B10
BUSAN : C10
DAEGU : D10
INCHEON : E10
GWANGJU : F10
DAEJEON : G10
ULSAN : H10
SEJONG : I10
GYEONGGI : J10
GANGWON : K10
CHUNGBUK : M10
CHUNGNAM : N10
JEONBUK : P10
JEONNAM : Q10
GYEONGBUK : R10
GYEONGNAM : S10
JEJU : T10
FORIENGER : V10
"""
R_SEOUL = "B10"
R_BUSAN = "C10"
R_DAEGU = "D10"
R_INCHEON = "E10"
R_GWANGJU = "F10"
R_DAEJEON = "G10"
R_ULSAN = "H10"
R_SEJONG = "I10"
R_GYEONGGI = "J10"
R_GANGWON = "K10"
R_CHUNGBUK = "M10"
R_CHUNGNAM = "N10"
R_JEONBUK = "P10"
R_JEONNAM = "Q10"
R_GYEONGBUK = "R10"
R_GYEONGNAM = "S10"
R_JEJU = "T10"
R_FORIENGER = "V10"


def get_region_name(region):
    regions = {
        'B10': 'SEOUL',
        'C10': 'BUSAN',
        'D10': 'DAEGU',
        'E10': 'INCHEON',
        'F10': 'GWANGJU',
        'G10': 'DAEJEON',
        'H10': 'ULSAN',
        'I10': 'SEJONG',
        'J10': 'GYEONGGI',
        'K10': 'GANGWON',
        'M10': 'CHUNGBUK',
        'N10': 'CHUNGNAM',
        'P10': 'JEONBUK',
        'Q10': 'JEONNAM',
        'R10': 'GYEONGBUK',
        'S10': 'GYEONGNAM',
        'T10': 'JEJU',
        'V10': 'FORIENGER'
    }

    return regions[region]