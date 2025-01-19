# import random


# Aufgabe 1
# Schreibe eine for Schleife, die die Summe aller Zahlen von 1 bis 100
# berechnet und das Ergebnis ausgibt

# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
# print(sum(list(i for i in range(1, 101))))
# print(sum([i for i in range(1, 101)]))

# Aufgabe 2
# Schreibe ein Programm, das eine Liste von Benutzernamen durchläuft und
# überprüft ob sie gültig sind Ein Benutzername ist nur gültig, wenn er
# länger als 3 Zeichen ist und keine Leerzeichen enthält


# benutzer_name = ['Mike', 'Evander', 'Ali']
# for name in benutzer_name:
#     if len(name) > 3 and ' ' not in name:
#         print(f"Der Name {name} die Benutzer sind gultig")
#     else:
#         print(f"Der Name {name} die Benutzer sind ungultig")


# Aufgabe 3
# Erstelle ein Programm, das eine Einkaufsliste verwaltet. Es sollte
# Artikel von einer Liste entfernen, wenn sie bereits gekauft wurden. Verwende
# dazu eine Schleife, um den Benutzer zu fragen,
# welchen Artikel er gekauft hat, und entferne diesen dann aus der Liste.


# einkaufliste = ['apple', 'banana', 'milk', 'coffee']
# for i in range(len(einkaufliste)):
#     gekauft = input("Was hast du bereit gekauft?: ")
#     index = einkaufliste.index(gekauft)
#     del einkaufliste[index]
#     print(einkaufliste)


# Aufgabe 4
# Schreibe ein Programm, das so lange Noten (Zahlen zwischen 1 und 6) vom Benutzer
# entgegennimmt, bis der Benutzer "0" eingibt.
# Anschließend soll das Programm die Durchschnittsnote berechnen und ausgeben.


# noten = []
# while True:
#     print("Geben Sie bitte ein Numer zwieschen 1 und 6. Geben 0 fur Ausgang.")
#     num = int(input())
#     if num < 0 or num > 6:
#         continue
#     elif num == 0:
#         print(len(noten))
#         print(sum(noten) / len(noten))
#         break
#     else:
#         noten.append(num)


# Aufgabe 5
# Schreibe ein Programm, das eine zufällige Zahl zwischen 1 und 20 generiert.
# Der Benutzer soll die Zahl erraten. Wenn der Benutzer richtig rät, beende die Schleife.
# Ansonsten gib Hinweise aus, ob die Zahl zu hoch oder zu niedrig ist.


# zahl = random.randint(1, 20)
# print("Raten Sie bitte die Zahl von 1 bis 20")
# try:
#     while True:
#         rat = int(input("Ihre Zahl:  "))
#         if rat == zahl:
#             print("Sie haben geratet")
#             break
#         else:
#             continue
# except ValueError as e:
#     print(e)
# print("Die Zahl war", zahl)


# Aufgabe 6
# Schreibe ein Programm, das vom Benutzer eine Reihe von Zahlen entgegennimmt.
# Verwende eine Schleife, um diese Eingaben zu verarbeiten und negative Zahlen herauszufiltern.
# Gib nur die positiven Zahlen in einer Liste aus.


# neu_list = []
# zahle = [int(input()) for i in range(5)]
# for i in range(5):
#     zahle.append(int(input("Bitte geben die Zahle ein: ")))
#
# for i in zahle:
#     if i % 2 == 0:
#         neu_list.append(i)
#     else:
#         continue
# print(neu_list)


# Aufgabe 7
# Baue eine Liste mit 8 Namen
# Schreibe ein Programm mit einer Funktion, welche einen Namen in einer
# Namensliste sucht, benutze hierfür eine Schleife die durch die Liste iteriert.
# Der Benutzer soll einen Namen in einem Input angeben können.
# Wenn du den Namen gefunden hast, füge dem Namen den Satz: "ist 25 Jahre alt"
# durch einen weiteren Input hinzu und speichere den Namen mit dem Alter in der Liste
# verwende die time.sleep() Methode um eine Bearbeitungszeit zu simulieren
# nach der simulation der Bearbeitungszeit, gib deine aktualisierung aus.
# Wenn der Name nicht in der Liste ist, gib aus, das der Name in er Liste nicht vorhanden ist

import time

liste = ['Pavlo', 'Tobias', 'Mahmoud', 'Maximilian',
        'Alan', 'Volkan', 'Beata', 'Ronja']

while True:
    user_input = input("Bitte geben ein Name ein: ")
    if user_input in liste:
        alter_input = input("Geben Alter bitte: ")
        time.sleep(1)
        print(user_input, 'is', alter_input, 'old')
        break
    print("Der Name existiert in der Liste nicht")

    # for name in liste:
    #     if name == user_input:
    #         alter_input = input("Geben Alter bitte: ")
    #         # time.sleep(1.5)
    #         print(user_input, 'is', alter_input, 'old')
    #         break
