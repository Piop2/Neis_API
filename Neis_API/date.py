from datetime import datetime

class Date:
    _year: int
    _month: int
    _day: int

    def __init__(self, year: int, month: int, day: int) -> None:
        self._year = year
        self._month = month
        self._day = day

    @staticmethod
    def today() -> Date:
        today = datetime.today()
        return Date(year=today.year, month=today.month, day=today.day)

    def __str__(self):
        return "%i.%02d.%02d" % (self.year, self.month, self.day)

    @property
    def y(self) -> int:
        return self._year

    @property
    def m(self) -> int:
        return self._month

    @property
    def d(self) -> int:
        return self._day

    def _get(self) -> str:
        return "%i%02d%02d" % (self.year, self.month, self.day)
