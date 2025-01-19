from datetime import date, datetime, time

my_datetime = datetime(2021, 12, 21)
print(my_datetime.strftime('%d-%b-%Y'))
print(my_datetime.strftime('%d/%m/%Y'))

date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)