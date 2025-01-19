from pathlib import Path


# Aufgabe 1
# Schreibe ein Programm, das den Benutzer auffordert, eine ganze Zahl
# einzugeben und diese Zahl verdoppelt.
# Verwende deine Kenntnisse im Error Handling, um eine ValueError
# exception abzufangen, falls der Benutzer
# etwas anderes als eine Zahl eingibt.


# try:
#     user_input = int(input("Geben Sie bitte ein Zahl:\t"))
#     print(user_input * 2)
# except ValueError as e:
#     print(e)


# Aufgabe 2
# Schreibe eine Funktion mit dem Namen addieren(a, b),
# die zwei Zahlen als Parameter empfängt.
# Verwende deine Error Handling Skills, um einen TypeError
# abzufangen, falls einer der Parameter
# kein Zahlentyp ist

# def addieren(a, b):
#     try:
#         print(a + b)
#     except TypeError as e:
#         print(e)
#
#
# addieren(1, 2)


# Aufgabe 3
# Schreibe eine Funktion mit dem Namen teilen, die 2 Zahlen
# als Parameter erhält und das Ergebnis einer
# Division zurück gibt. Verwende try und except um eine
# Division durch Null zu verhindern und eine
# entsprechende Fehlermeldung auszugeben


# def teilen(a, b):
#     try:
#         print(a / b)
#     except ZeroDivisionError as e:
#         print(e)
#
#
# teilen(4, 0)


# Aufgabe 4
# Du findest eine Liste mit 5 Zahlen. Der
# Benutzer soll einen Index eingeben
# und das Programm gibt das Element an dieser
# Position aus. Verwende Error Handling um einen
# IndexError und einen ValueError abzufangen,
# wenn der Benutzer keinen gültigen Index eingibt
# (Am liebsten durch eine seperate exception)


# numbers = [10, 20, 30, 40, 50]
# def func():
#     try:
#         user_input = int(input("Number please:\t"))
#         print(numbers[user_input])
#     except IndexError as e:
#         print('IndexError', e)
#     except ValueError as e:
#         print('ValueError', e)
#
#
# func()


# Aufgabe 5
# Wenn der Benutzer einen Namen eingibt, der
# nicht im Dictionary existiert, soll eine Meldung
# "Fehler: Name nicht gefunden!" ausgegeben werden.
# Verwende KeyError.


# mitarbeiter = {
#     "Daniel": 25,
#     "Lukas": 30,
#     "Serhat": 15,
#     "Georg": 66,
#     "Mandy": 11,
# }
# user_input = input("Name please:\t")
# try:
#     print(mitarbeiter[user_input])
# except KeyError:
#     print("Fehler: Name nicht gefunden!")


# Aufgabe 6
# Schreibe ein Programm, dass eine Datei mit dem Namen
# rechnung.txt öffnet und deren Inhalt auf dem Bildschirm ausgibt
# Erstelle einen Ordner mit dem Namen dateien. Speichere
# darin eine Datei namens rechnung.txt und finde heraus wie
# du die Datei öffnen und in der Print ausgabe lesen kannst.
# Verwende FileNotFoundError, wenn die Datei nicht existiert.


# try:
#     file_path = Path.open("C://Python//my_project")
#     with open(file_path / "rechnung.txt", "r") as file:
#         reader = file.read(file)
#         print(reader)
# except FileNotFoundError as e:
#     print(e)


# Aufgabe 7
# Schreibe ein Programm, welches eine Datei mit dem Namen Test
# in deinem Ordner dateien speichert und schreibe eine kleine
# Geschichte dort hinein. Finde heraus, welcher Modus für das
# schreiben von Dateien genutzt werden kann.
# Was wäre ein alternativer Modus, wenn du etwas an die Datei
# anhängen willst ohne die Datei bei dem erneuten ausführen zu
# überschreiben?

# import sys
# try:
#     with open('Test.txt', 'w') as date:
#         date.write("""Aufgabe 7
# Schreibe ein Programm, welches eine Datei mit dem Namen Test
# in deinem Ordner dateien speichert und schreibe eine kleine
# Geschichte dort hinein. Finde heraus, welcher Modus für das
# schreiben von Dateien genutzt werden kann.
# Was wäre ein alternativer Modus, wenn du etwas an die Datei
# anhängen willst ohne die Datei bei dem erneuten ausführen zu
# überschreiben?""")
# except:
#     print("Datei nicht geoffnet")
#     sys.exit(0)




# Aufgabe 8
# Schreibe ein Programm, das die Variable namens zahl verwendet
# und diese mit einem Wert von 10 Multipliziert.
# Verwende Error Handling um einen NameError abzufangen, für den
# Fall, das die Variable nicht definiert wurde.


# try:
#     zahl = int(input("Zahl bitte:\t"))
#     print(zahl * 10)
# except ValueError as e:
#     print('ValueError', e)
# except TypeError as e:
#     print('TypeError', e)
# except NameError as e:
#     print('NameError', e)


# Aufgabe 9
# Schreibe ein Programm, das eine einfache Benutzerverwaltung in
# einem Dictionary simuliert. Frage den Benutzer ob er sich
# anmelden, Registrieren oder das Programm beenden möchte.
# Eine Registrierung wird in einem Dictionary gespiechert
# mit einem Namen und dem Alter
# Fange folgende Fehler ab:
# Der Name darf nicht leer sein und das Alter muss
# eine ganze Zahl sein.
# Wenn der Benutzer sich anmelden möchte,
# muss er nur seinen Namen eingeben.
# Wenn der Benutzer im Dicitonary vorhanden ist,
# gib seinen Namen und sein Alter aus.
# Wenn der Benutzer nicht im Dictionary gefunden wird,
# wird eine Fehlermeldung angezeigt durch einen KeyError.


# user_database = {}
#
#
# def abfrage_benutzer():
#     while True:
#         user_input = int(input("""Herzlich Willkommen:
# möchten Sie sich Anmelden dann geben Sie -1-
# möchten Sie sich Registrieren dann geben Sie -2-
# möchten Sie das Programm beenden dann geben Sie -3-\n"""))
#
#         if user_input == 1:
#             name_benutzer = input("Ihre Name bitte:\t")
#             anmelden_benutzer(name_benutzer)
#         elif user_input == 2:
#             try:
#                 name_benutzer = input("Ihre Name bitte:\t")
#                 alter_benutzer = int(input("und Ihre Alter bitte:\t"))
#                 registriren_benutzer(name_benutzer, alter_benutzer)
#                 print(user_database)
#             except ValueError as e:
#                 print("ValueError", e)
#             except TypeError as e:
#                 print("TypeError", e)
#         else:
#             print("Das Programm ist beenden")
#             exit(0)

#
# def anmelden_benutzer(name):
#     try:
#         if name in user_database:
#             print(f"{name} und sein Alter {user_database[name]}")
#     except KeyError as e:
#         print("KeyError", e)
#     print(f"Es gibt kein Benutzer mit dem Name {name}")
#
#
# def registriren_benutzer(name, alter):
#     user_database[name] = alter
#     # print("N")
#
#
# abfrage_benutzer()
