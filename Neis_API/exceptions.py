class DateRangeError(Exception):
    def __init__(self):
        super().__init__("Date range could be start_date~end_date or date")
        return


class UnkownErrorCode(Exception):
    def __init__(self, error_code: str):
        super().__init__("Unkown service error: %s" % error_code)
        return
