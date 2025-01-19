# Aufgabe 1
# Erstelle eine Liste von Quadratzahlen der Zahlen von 1 bis 20

import time
import random
eine_liste = [i * i for i in range(1, 21)]
print(eine_liste)

# Aufgabe 2
# Hier ist eine Liste von graden Zahlen. Verwende eine List Comprehension um nur die
# graden Zahlen herauszufiltern

zahlen = [10, 15, 23, 42, 55, 68, 73, 80, 87, 93, 96, 99, 110, 111, 120]
grade_zahle_list = [i for i in zahlen if i % 2 == 0]
print(grade_zahle_list)

# Aufgabe 3
# Du findest eine Variable vom Datentyp String, Erstelle eine neue Liste die nur die
# Vokale a, e, i, o, u aus dem String enthält

satz = "Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo"
vokale_liste = [i for i in satz if i == 'a' or i == 'e' or
                i == 'i' or i == 'o' or i == 'u']
print(vokale_liste)

# Aufgabe 4
# Erstelle eine Liste mit den Zahlen 1 bis 100, aber nimm nur die Zahlen auf, welche durch 5 oder 7 teilbar sind

zweite_liste = [i for i in range(1, 101) if i % 5 or i % 7]

# Aufgabe 5
# Du findest eine Liste mit Wörtern. Erstelle eine neue Liste die nur Wörter enthält die länger als 4
# Zeichen lang sind

woerterliste = ['Apfel', 'Ei', 'Banane', 'Traube',
                'Ananas', 'Kiwi', 'Uwe', 'Rettungswagen', 'Schlafmütze']
neu_woerter_liste = [wort for wort in woerterliste if len(wort) > 4]

# Aufgabe 6
# Du findest einen Satz. Erstelle eine Liste, die die Länge jedes Wortes in diesem Satz erhält

satz = "Ihr werdet besser und besser. Hört nicht auf zu lernen, ihr seid richtig gut <3"
lange_liste = [len(i) for i in satz.split()]
print(lange_liste)

# Aufgabe 7
# Erstelle eine Liste der Quadratzahlen von 1 bis 50, aber nur für ungrade Zahlen

quad_liste = [i * i for i in range(1, 50) if i % 2 != 0]
print(quad_liste)

# Aufgabe 8
# Du findest eine Liste mit Wörtern. Erstelle eine Liste, in der jedes Wort in Großbuchstaben umgewandelt wird

wortliste = ["Das", "ist", "eine", "sehr", "einfache", "Übung",
             "um", "dir", "das", "Leben", "schwer", "zu", "machen"]
gross_buchschtaben_liste = [wort.capitalize() for wort in wortliste]
print(gross_buchschtaben_liste)

# Aufgabe 9
# Du findest 2 Listen. Erstelle eine neue Liste von Tupeln, die alle
# Kombinationen von Zahl und Buchstaben enthalten

zahlen = [1, 2, 3]
buchstaben = ['A', 'B', 'C']

new_list = tuple(zip(zahlen, buchstaben))
print(new_list)

new_list_2 = ((zahlen[i], buchstaben[i]) for i in range(3))
print(new_list_2)

new_list_3 = [(x, y) for x in zahlen for y in buchstaben]
print(new_list_3)


# Aufgabe 10
# Du findest eine Liste mit 1000 Namen. Baue ein Programm, in dem ein
# Benutzer einen Namen eingeben muss. Benutze die List Comprehension dazu,
# die Namensliste nach dem Namen zu durchsuchen unabhängig davon, ob der
# Benutzer den Namen groß oder kleinschreibt.
# Messe die Zeit wie lange deine List Comprehension dafür benötigt hat.

vornamen = ["Anna", "Ben", "Clara", "David", "Eva", "Felix", "Greta", "Hannes", "Iris", "Jonas",
            "Klara", "Lukas", "Maria", "Nina", "Oskar", "Paula", "Quentin", "Rosa", "Sebastian", "Tina",
            "Uwe", "Vera", "Walter", "Xenia", "Yannik", "Zoe"]

nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker",
             "Schulz", "Hoffmann", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder",
             "Neumann", "Schwarz", "Zimmermann", "Krüger", "Hartmann", "Lange", "Werner", "Schmitz"]

namen_liste = [f"{random.choice(vornamen)} {
    random.choice(nachnamen)}" for _ in range(1000)]
print(namen_liste)

name = input("Please enter a name:  ").lower()
start_time = time.time()
print(start_time)
find_name = [the_name for the_name in namen_liste if the_name.lower() == name]
end_time = time.time() - start_time
print(find_name, end_time)
print(len(find_name))
print(time.time())
