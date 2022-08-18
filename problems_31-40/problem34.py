import calendar
import datetime
year,month,day=input("What is the date in YYYY-MM-DD: ").split('-')
valid=True
try:
    date = datetime.date(int(year),int(month),int(day))
except ValueError:
    print("Invalid date")
    valid=False

if valid:
    print(calendar.day_name[date.weekday()])