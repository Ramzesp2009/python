print("Tag des Datums eingeben:")
tag = int(input())
print("Monat des Datums eingeben:")
monat = int(input())
print("Jahr des Datums eingeben:")
jahr = int(input())
richtig = True

if 1 < tag > 31 or 1 < monat > 12:
    richtig = False

if monat == 4 or monat == 6 or monat == 9 or monat == 11:
    print("Der letzter Tag ist 30")
    if tag > 30:
        richtig = False
elif monat == 2:
    if jahr%4 == 0 and jahr%100 !=0 or jahr%400 == 0:
        print("Der letzter Tag ist 29")
        if tag > 29:
            richtig = False
    else:
        print("Der letzter Tag ist 28")
        if tag > 28:
            richtig = False
else:
    print("Der letzter Tag ist 31")

if richtig:
    print("Gultiges Datum")
else:
    print("Ungultiges Datum")