from datetime import timedelta, datetime

my_datetime = datetime(2021, 12, 21, 12, 00, 00)
print(my_datetime)
print(timedelta)
print(my_datetime - timedelta(days=100, hours=120))
print(my_datetime + timedelta(days=100, hours=120))