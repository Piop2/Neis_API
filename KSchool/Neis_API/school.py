class School:
    _region_code: str
    _school_code: str

    def __init__(self, region_code, school_code):
        self._region_code = region_code
        self._school_code = school_code

    @classmethod
    def search_name(cls):...

    def meal_date(self, date):...

    def meal_daterange(self, start_date, end_date):...
