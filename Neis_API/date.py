from datetime import datetime


class Date:
    def __init__(self, year, month, day):
        self._year = int(year)
        self._month = int(month)
        self._day = int(day)

    @staticmethod
    def today():
        today = datetime.today()
        return Date(today.year, today.month, today.day)

    def __str__(self):
        return "%i.%02d.%02d" % (self.year, self.month, self.day)

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    def get(self):
        return "%i%02d%02d" % (self.year, self.month, self.day)
