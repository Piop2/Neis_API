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
