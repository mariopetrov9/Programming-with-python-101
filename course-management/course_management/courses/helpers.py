from datetime import datetime

NUMBER_LECTIONS = 3


def calc_duration(date1, date2):
    parsed_start = datetime.strptime(date1, "%Y-%m-%d")
    parsed_end = datetime.strptime(date2, "%Y-%m-%d")
    return (parsed_end.year - parsed_start.year)*12 + parsed_end.month - parsed_start.month


