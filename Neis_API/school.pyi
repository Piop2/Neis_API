from typing import overload

import date


class School:
    _region:str
    _code:str
    _key:str
    @overload
    def __init__(self, region:str, school_code:str, key:str=None) -> None: ...
    @property
    def region_code(self) -> str: ...
    @property
    def region_name(self) -> str: ...
    @property
    def school_code(self) -> str: ...
    @classmethod
    def find(cls, region_code:str, school_code:str=None, school_name:str=None, key:str=None) -> School: ...
    @overload
    def get_meal(self, date:str, pindex:int=1, psize:int=100) -> None: ... # 아아아앙
    @overload
    def get_meal(self, start_date:str, end_date:str, pindex:int=1, psize:int=100) -> None: ...
    @overload
    def get_meal(self, date:date.Date, pindex:int=1, psize:int=100) -> None: ... # 아아아앙
    @overload
    def get_meal(self, start_date:date.Date, end_date:date.Date, pindex:int=1, psize:int=100) -> None: ...
