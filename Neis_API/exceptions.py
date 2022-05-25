class DateRangeError(Exception):
    def __init__(self):
        super().__init__("Date range could be start_date~end_date or date")
        return
