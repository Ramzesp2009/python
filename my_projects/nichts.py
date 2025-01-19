def summe(a, b):
    c = a + b
    # return c

# Programm
erg = summe(7, 12)
if not erg:
    print("Fehler")
if erg is None:
    print("Fehler")
print("Ergebnis:", erg)
print("Wahrheitswert:", bool(erg))
print("Typ:", type(erg))