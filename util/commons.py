import datetime


class Commons:
    PATTERN_FORMAT = "yyyy-MM-dd"

    @staticmethod
    def to_instant(date_str):
        date = datetime.datetime.strptime(date_str, Commons.PATTERN_FORMAT).date()
        return date.strftime("%s")

    @staticmethod
    def format_instant(instant: datetime):
        unix_timestamp = instant.timestamp()
        return datetime.datetime.fromtimestamp(unix_timestamp).strftime(Commons.PATTERN_FORMAT)

    @staticmethod
    def to_string():
        return f"Commons{{dateFormatter={Commons.PATTERN_FORMAT}, " \
               f"instantFormatter={Commons.PATTERN_FORMAT}, " \
               f"formatInstant=<function Commons.format_instant at {id(Commons.format_instant)}>}}"
