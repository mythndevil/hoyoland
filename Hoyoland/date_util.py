
import datetime


def get_today():
    today = datetime.date.today()
    return today.strftime("%Y%m%d")


def get_one_day_later(date):
    day = datetime.datetime.strptime(date, "%Y%m%d")
    one_day_later = day + datetime.timedelta(days = 1)
    return one_day_later.strftime("%Y%m%d")


