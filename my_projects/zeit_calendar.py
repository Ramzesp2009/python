import calendar, datetime

print('Schaltjahr:', calendar.isleap(2024))
print("Anzahl Schaltjahre:", calendar.leapdays(2020, 2030))
print()

calendar.prmonth(2024, 10)
print()

print("Volle Wochen:")
cal = calendar.Calendar()
it = cal.itermonthdates(2024, 2)
for datum in it:
    print(datum.strftime("%d.%m."), end=" ")
    if datum.isoweekday() == 7:
        print()
print()

print("Enumeration uber Wochentage:")
for tag in calendar.Day:
    print(tag, end=" ")
print()

if calendar.weekday(2024,2,1) == calendar.THURSDAY:
    print("01.02.2024 ist ein Donnerstag")
print()

print("Enumeration uber Monate:")
for monat in calendar.Month:
    print(monat, end=" ")
print()

d = datetime.datetime(2024, 2, 1)
if d.month == calendar.FEBRUARY:
    print("Monat ist Februar")
