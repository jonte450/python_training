import calendar


def print_calendar(year, month):

    num_days = calendar.monthrange(year,month)[1]

    month_name = calendar.month_name[month]
    print(f"Calendar for {month_name} {year}")
    print(f"Number of days: {num_days}")
    print("-----------------------------")


year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

print_calendar(year,month)