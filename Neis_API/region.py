R_SEOUL: str = "B10"
R_BUSAN: str = "C10"
R_DAEGU: str = "D10"
R_INCHEON: str = "E10"
R_GWANGJU: str = "F10"
R_DAEJEON: str = "G10"
R_ULSAN: str = "H10"
R_SEJONG: str = "I10"
R_GYEONGGI: str = "J10"
R_GANGWON: str = "K10"
R_CHUNGBUK: str = "M10"
R_CHUNGNAM: str = "N10"
R_JEONBUK: str = "P10"
R_JEONNAM: str = "Q10"
R_GYEONGBUK: str = "R10"
R_GYEONGNAM: str = "S10"
R_JEJU: str = "T10"
R_FORIENGER: str = "V10"


def region_name(region: str) -> None:
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
