import random
random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print(f"Die Aufgabe: {a} + {b}")

zahl = 0
versuch = 0
while zahl != c:
    versuch += 1
    print("Bitte Losungsvorschlag eingeben:")
    zahl = int(input().strip())
    if zahl == c:
        print(zahl, "ist richtig")
    else:
        print(zahl, "ist falsch")

print("Ergebnis:", c)
print("Anzahl der Versuche:", versuch)