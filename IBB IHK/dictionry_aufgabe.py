# Aufgabe 1
# Erstelle ein Dictionary, das die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.


# noten_dict = {
#     'math': {'evan': 4, 'elise': 3, 'mark': 5, 'jenifer': 4},
#     'chemie': {'evan': 4, 'elise': 3, 'mark': 5, 'jenifer': 4},
#     'biologie': {'evan': 4, 'elise': 3, 'mark': 5, 'jenifer': 4}
# }
#
# def look_for_subject(name_subject):
#     if name_subject in noten_dict:
#         print(noten_dict.get(name_subject))
#     else:
#         print("There isn't the subject in the list")
#
#
# user_input = input("Please enter a subject's name:\t")
# look_for_subject(user_input)


# AUfgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )

# mitarbeiter = {
#     "Max Mustermann": "Geschäftsführer",
#     "Anna Meier": "Marketing Managerin",
#     "Peter Schmidt": "Softwareentwickler",
#     "Lisa Müller": "Personalreferentin",
#     "David Neumann": "Finanzbuchhalter"
# }
#
# def look_for_worker(name):
#     if name in mitarbeiter:
#         print(f"{name} works as {mitarbeiter.get(name)}")
#     else:
#         print("There isn't a worker with such name")
#
#
# user_input = input("Please enter a employee's name:\t")
# look_for_worker(user_input)


# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion,
# die neue Produkte und deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde,
# soll der Artikel gespeichert werden und einen Standardpreis von 0 zurückgegeben

# lebensmittel_preise = {
#     "Apfel": 1.29,
#     "Banane": 0.89,
#     "Tomate": 2.49,
#     "Brot": 2.99,
#     "Milch": 1.59
# }
#
# def create_new_product():
#     name = input("Please enter a new product:\t").capitalize()
#     if name not in lebensmittel_preise:
#         lebensmittel_preise[name] = 0
#     else:
#         print("The product is already in list")
#         print(lebensmittel_preise[name])
#     print(lebensmittel_preise.items())
#
#
# create_new_product()


# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen.
# Schreibe ein Programm, das durch die Schlüssel des
# Dictionaries iteriert und nur die Namen der Personen ausgibt

# personen = {
#     "Max Mustermann": 30,
#     "Anna Meier": 25,
#     "Peter Schmidt": 35
# }
#
# for key in personen:
#     print(key)


# Aufgabe 5
# Gegeben ist ein Dictionary, das die Lagerbestände eines Geschäfts speichert.
# Schreibe ein Programm, das alle Artilkel ausgibt, die aktuell im Lager sind
# (Tipp: Schlüssel mit Wert > 0)


# articles = {
#     "Screws": 10000,
#     "Wood": 0,
#     "Nails": 100,
#     "toolkit": 10,
#     "scanner": 2,
#     "paper": 0,
# }
#
# for i, j in articles.items():
#     if j > 0:
#         print(f"Name - {i} | quantity - {j}")

# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt

# countries = {
#     "Deutschland": 85000000,
#     "Frankreich": 68000000,
#     "Spanien": 47000000,
#     "Polen": 36000000,
# }
# countries_list = [key for key in countries]
# countries_list.sort()
# print(countries_list)

# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren
# Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary
# berechnet und ausgibt.

# tierbestand = {
#     "Hunde": 15,
#     "Katzen": 22,
#     "Vögel": 8,
#     "Fische": 50,
#     "Hamster": 12
# }
#
# def quantity_available_animal(animal_name):
#     quantity_animal = 0
#     for i, j in tierbestand.items():
#         quantity_animal += j
#     return quantity_animal
#
# qty = quantity_available_animal(tierbestand)
# print(qty)


# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())


# students = {
#     "Alan": 1,
#     "Jacques": 6,
#     "Gerhard": 1,
#     "Willi": 4,
#     "Susanne": 2
# }
# average = 0
# for i in students.values():
#     average += i
# print(average / len(students))


# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener
# Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten
# Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt

# umsatz_filialen = {
#     "Berlin": 120000,
#     "München": 150000,
#     "Hamburg": 110000,
#     "Köln": 95000
# }
#
#
# def max_umsatz(filials):
#         values_list = [values for values in filials.values()]
#         max_usatz = max(values_list)
#         for key, values in filials.items():
#             if values == max_usatz:
#                 print("höchsten Umsatz - ", end='')
#                 print(key, values)
#
# max_umsatz(umsatz_filialen)



# Aufgabe 10
# Erstelle ein Wörterbuch, welches die Preise von 5 Artikeln
# speichert. Verwende items() um durch die Schlüssel Wert Paare zu iterieren
# und alle Artikel, deren Preis über 10 € liegt, auszugeben

# lebensmittel_preise = {
#     "Apfel": 10.29,
#     "Banane": 9.89,
#     "Tomate": 12.49,
#     "Brot": 21.99,
#     "Milch": 7.59
# }
# for key, value in lebensmittel_preise.items():
#     if value > 10:
#         print(key, '-', value)


# Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern
# in einem Videospiel speichert. Der Spielername ist der
# Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm,
# welches den Spieler ausgibt, der die höchste Punktzahl hat. (Benutze items())

# spieler_punkte = {
#     "Spieler1": 1200,
#     "Spieler2": 850,
#     "Spieler3": 1550
# }
#
#
# def max_punktzahl(game_score):
#     values_list = [values for values in game_score.values()]
#     max_score = max(values_list)
#     for key, values in game_score.items():
#         if values == max_score:
#             print("Maximal Score - ", end='')
#             print(key, values)
#
#
# max_punktzahl(spieler_punkte)


# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film
# (z.B.: Titel, Jahr, Genre). Schreibe ein Programm, dass das Dictionary
# mithilfe von update um die Bewertung des Films erweitert.

# film = {
#     "Titel": "Der Herr der Ringe: Die Gefährten",
#     "Jahr": 2001,
#     "Genre": "Fantasy",
#     "Regisseur": "Peter Jackson",
#     "Hauptdarsteller": ["Elijah Wood", "Ian McKellen", "Viggo Mortensen"]
# }
#
# def bewertung_einen_film(another_dict):
#     for key in another_dict.keys():
#         if key not in film:
#             film.update(another_dict)
#     print(film)
#
# bewertung_einen_film({'bewertung': 7.9})


# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in
# zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm, dass den Lagerbestand der beiden
# Filialen zusammenführt (benutze Update) und gib das
# kombinierte Dictionary aus

# Filiale 1
# filiale1 = {
#     "Apfel": 100,
#     "Banane": 50,
#     "Birne": 30,
#     "Orange": 80,
#     "Grape": 14,
#     "Strawberry": 46
# }

# Filiale 2
# filiale2 = {
#     "Apfel": 120,
#     "Banane": 75,
#     "Birne": 45,
#     "Orange": 90,
#     "Kiwi": 60,
#     "Raspberry": 98,
#     "Pineapple": 77
# }
#
# def union_quantity_two_filials(fil_1, fil_2):
#     union_dict_of_filials = {}
#     for key, value in fil_1.items():
#         if key in fil_2:
#             union_dict_of_filials[key] = fil_1[key] + fil_2[key]
#         else:
#             union_dict_of_filials[key] = value
#     for key, value in fil_2.items():
#         if key not in fil_1:
#             union_dict_of_filials[key] = value
#     print(union_dict_of_filials)
#
# union_quantity_two_filials(filiale1, filiale2)


# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen
# Schreibe ein Programm, das den Benutzer auffordert, den Preis
# eines Produkts zu aktualisieren. Verwende update() um das
# Produkt mit dem neuen Preis im Dictionary zu aktualisieren.


# lebensmittel_preise = {
#     "Apfel": 1.29,
#     "Banane": 0.89,
#     "Tomate": 2.49,
#     "Brot": 2.99,
#     "Milch": 1.59
# }
# name_fruit = input("Please name a fruit:\t")
# new_price = input("Please give a new price:\t")
# temp_dict = {name_fruit: new_price}
# def update_lebensmittel_preise(temp_dict):
#     new_lebensmittel_price = lebensmittel_preise.copy()
#     new_lebensmittel_price.update(temp_dict)
#     return new_lebensmittel_price
#
#
# print(update_lebensmittel_preise(temp_dict))


# Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden
# und deren Handynummern. Schreibe ein Programm,
# dass das Dictionary mit clear() leert und überprüft, ob es nun leer ist.


# klassenkameraden = {
#     "Max Mustermann": "01711234567",
#     "Maria Meier": "01519876543",
#     "Lisa Schmidt": "01601234567"
# }
#
# def clear_phone_book(phone_book):
#     clear_book = phone_book.copy()
#     clear_book.clear()
#     if not clear_book:
#         print("Phone book is empty")
#         print(clear_book)
#
#
# clear_phone_book(klassenkameraden)


# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.
# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note
# nach der Eingabe eines Benutzers in dem Dictionary speichert,
# allerdings nur, wenn weniger als
# 5 Studenten in dem Dictionary gespeichert sind.
# Aufgabe 16.2
# Falls schon 5 Studenten in dem Dictionary gespeichert sind,
# weise darauf hin, dass schon 5 Studenten gespeichert sind und
# stelle den Benutzer vor eine Wahl, ob er das aktuelle Dictionary
# löschen möchte um den neuen Studenten dort abspeichern zu können,
# gib währenddessen den Notendurchschnitt aller Studenten aus.
# Aufgabe 16.3
# Wenn der Benutzer sich gegen das Löschen der Daten entscheidet, beende das Programm.
# Aufgabe 16.4
# Wenn der Benutzer die Daten löschen will, rufe eine neue Funktion
# die du jetzt neu bauen wirst, auf welche als Parameter die Daten
# des neuen Studenten als Dictionary empfängt,
# Aufgabe 16.5
# lösche in deiner neuen Funktion, die du sinnvoll benannt hast alle
# Daten in dem Dictionary student_graduations
# Aufgabe 16.6
# Stelle den Benutzer noch einmal in deiner neuen Funktion vor eine Auswahl,
# ob er die Daten die du Übergeben hast, in dem Dictionary student_graduations
# speichern will. Entscheidet sich der Benutzer die Daten zu speichern, speichere die neuen
# Daten in dem Dictionary und gib dein Dictionary aus. Entscheidet sich der
# Nutzer gegen das speichern, sollte ein leeres Objekt angezeigt werden
# hat Kontextmenü

# studenten_noten = {
#     "Max Mustermann": 5,
#     "Maria Meier": 2,
#     "Lisa Schmidt": 8,
#     "Tim Müller": 6,
#     "Anna Nowak": 9
# }
#
# def add_new_student():
#     name_new_student = input("Name the new student:\t").capitalize()
#     note_new_student = float(input("Note the new student:\t"))
#     if len(studenten_noten) < 5:
#         studenten_noten[name_new_student] = note_new_student
#     else:
#         print("There no place for new student")
#         clear_dict(name_new_student, note_new_student)
#     print(studenten_noten)
#
#
# def clear_dict(name: str, note: float):
#     average = 0
#     order = input("When you want it's possible to clear the"
#                   "student list with them note: Y / N ?\t").upper()
#     if order == 'Y':
#         for values in studenten_noten.values():
#             average += values
#         print("Notendurchschnitt aller Studenten sind", average / len(studenten_noten))
#         studenten_noten.clear()
#         print("The student note is empty")
#         answer = input("Do you really want to save the new student? Y/N?\t").upper()
#         if answer == 'Y':
#             studenten_noten[name] = note
#         else:
#             return "The student note is empty", studenten_noten
#
#     else:
#         return "Das programm sich geendet hat."
#
# if __name__ == '__main__':
#     add_new_student()