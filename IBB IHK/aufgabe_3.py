# Aufgabe 1
# Deklariere Variablen der folgenden primitiven Datentypen und weise passende Werte zu und gib sie aus:
# int, float, str, bool

# a = 1
# b = 1.2
# c = 'Hello'
# d = True

# Aufgabe 2
# Schreibe ein Programm, das zwei Ganzzahlen als Eingabe annimmt und folgende Berechnungen durchführt:
# Addition, Subtraktion, Multiplikation, division, modulo

# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

# Aufgabe 3
# Schreibe ein Programm, welches eine Fließkommazahl als Input annimmt und diesen
# Wert in einen Integer umwandelt.
# Danach soll das Programm prüfen ob der Integer Wert grade oder ungrade ist.

# a = float(input("Bitte eine Fließkommazahl eingeben: "))
# print(f"Als Integer wird es ", {int(a)})
# if a % 2 == 0:
#     print("Zahl ist grade")
# else:
#     print("Zahl ist ungrade")


# Aufgabe 4
# Schreibe ein Programm, welches das Alter einer Person abfragt und prüft, ob
# die Person volljährig ist oder nicht.
# Gib eine entsprechende Nachricht aus, ob Lina, die grade 14 geworden ist in
# die Discothek darf (Eintritt ab 18)

# age = int(input("Ihre Alter bitte: "))
# if age > 18:
#     print("Eintritt in die Diskothek erlaubt")
# else:
#     print("Eintritt in die Diskothek nicht erlaubt")

# Aufgabe 5
# Schreibe ein Programm, das drei Zahlen als Input entgegen nimmt und prüft,
# welche davon die größte ist.
# Gib die größte Zahl aus

# print(max(list(i for i in [int(input()) for i in range(3)])))


# Aufgabe 6
# Schreibe ein Programm, das zwei Ganzzahlen vergleicht und ausgibt, ob sie gleich sind, oder ob eine Zahl größer
# oder kleiner als die andere ist.

# zahl_1 = int(input("Zahl bitte eingeben: "))
# zahl_2 = int(input("Zahl bitte eingeben: "))
# if zahl_1 == zahl_2:
#     print("Zahl_1 und Zahl_2 ist gleich")
# elif zahl_1 > zahl_2:
#     print("Zahl_1 ist grosser als Zahl_2")
# else:
#     print("Zahl_1 ist kleiner als Zahl_2")

# Aufgabe 7
# Schreibe ein Programm welches prüft, ob eine Person Zugang zu einem System erhält.
# Die Person hat entweder die Rolle Admin oder Superuser oder das Passwort "secret" um auf das System zugreifen zu können
# Ansonsten wird der Zugriff verweigert benutze or

# Aufgabe 8
# Schreibe eine Funktion, die überprüft, ob eine gegebene Zahl sowohl größer als 10 als auch kleiner als 20 ist.
#  Verwende dafür bitte den and Operator und einen Input der eine Eingabe entgegen nimmt.
#
# def vergleich(x):
#     if 10 < x and x < 20:
#         print("Zahl ist mehr als 10 und kleiner als 20")
#     else:
#         print("Zahl ist kleiner als 10 oder grosser als 20")
#
# a = int(input("Bitte geben Sie eine Zahle ein: "))
# vergleich(a)

# Aufgabe 9
# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 0 oder
# größer als 100 ist. Verwende dabei den or Operator und einen Input für eine Eingabe

# def vergleich_2(x):
#     if x < 0 or x > 100:
#         print("Zahl ist mehr als 100 oder kleiner als 0")
#     else:
#         print("Zahl ist kleiner als 100 oder grosser als 0")
#
# a = int(input("Bitte geben Sie eine Zahle ein: "))
# vergleich_2(a)

# Aufgabe 10 Sonderaufgabe
# Schreibe ein Programm, das ein Passwort von einem Nutzer entgegen nimmt und überprüft
# ob es mindestens 8 Zeichen lang ist und es muss entweder eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten
# passwort = input("Bitte password: ")
# if len(passwort) > 8 and (
#         '%' in passwort or
#         '@' in passwort or
#         '#' in passwort or
#         '$' in passwort):
#     print("Password is good!")
# else:
#     print("Password is bad")
