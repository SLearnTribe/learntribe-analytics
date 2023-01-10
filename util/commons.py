import datetime


class Commons:
    PATTERN_FORMAT = "yyyy-MM-dd"

    def to_instant(self, date_str):
        date = datetime.datetime.strptime(date_str, self.PATTERN_FORMAT).date()
        return date.strftime("%s")

    def format_instant(self, instant):
        return datetime.datetime.fromtimestamp(int(instant)).strftime(self.PATTERN_FORMAT)

    def to_string(self):
        return f"Commons{{dateFormatter={self.PATTERN_FORMAT}, " \
               f"instantFormatter={self.PATTERN_FORMAT}, " \
               f"formatInstant=<function Commons.format_instant at {id(self.format_instant)}>}}"
