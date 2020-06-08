from datetime import datetime

print(datetime.now())

year = datetime.now().strftime("%Y")
print("year:", year)

month = datetime.now().strftime("%m")
print("month:", month)

week_number = datetime.now().strftime("%U")
print("week number:", week_number)

week_day = datetime.now().strftime("%w")
print("week day:", week_day )

day_of_year = datetime.now().strftime("%j")
print("day of the year:", day_of_year)

day_of_month = datetime.now().strftime("%d")
print("day of month:", day_of_month)

day_of_Week = datetime.now().strftime("%A")
print("day of WEEKDAY:", day_of_Week)