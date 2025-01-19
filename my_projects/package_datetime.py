from datetime import datetime, time, date

my_date = date(2022, 2, 24)
print(my_date)
print(my_date.isoformat())
print(my_date.year)
print(my_date.month)
print(my_date.day)

my_time = time(7, 34, 9)
print(my_time.isoformat())
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

my_datetime = datetime(2022, 12, 10, 16, 15, 30)
print(my_datetime.isoformat())
print(my_datetime.year)
print(my_datetime.month)
print(my_datetime.day)
print(my_datetime.hour)
print(my_datetime.minute)
print(my_datetime.second)
print(my_datetime.now().second)