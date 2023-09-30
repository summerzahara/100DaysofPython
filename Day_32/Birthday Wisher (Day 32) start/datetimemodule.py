import datetime as dt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
week_day = days[now.weekday()]
print(f"Now: {now}\nYear: {year}\nMonth: {month}\nDay: {day}\nWeek Day: {week_day}")

birthday = dt.datetime(year=1987, month=9, day=9)
print(f"My Birthday: {birthday}")
