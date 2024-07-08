import calendar
from datetime import datetime


def days_between_dates(start_date,end_date):
    start_datetime = datetime.strptime(start_date,'%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

    delta = end_datetime-start_datetime

    return delta.days

start_date = '2014-07-02'
end_date = '2014-07-11'


days = days_between_dates(start_date, end_date)

print("Number of days between", start_date, "and", end_date, "is:", days)
