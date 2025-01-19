# Was sind sets?
# Sets sind eine Sammlung von einzigartigen Werten
from pandas.core.computation.expr import intersection

set1 = {1, 2, 3, 4, 5}  # -> setzt ein direktes Set
set2 = {4, 5, 6}
set2 = set([4, 5, 6])  # -> umgewandeltes Set

set1.add(6)  # -> fügt die 6 zu dem Set1 hinzu
set1.remove(3)  # -> entfernt die 3 aus dem Set
set1.discard(
    10)  # -> discard entfernt ein Element, wirft aber keinen Fehler, wenn das Element nicht im Set vorhanden ist

all = set1.union(
    set2)  # -> vereint 2 sets, wobei die doppelten Werte auf jeweils nur einen vorhandenen Wert reduziert werden.
gemeinsame_elemente = set1.intersection(set2)  # -> erstellt eine Schnittmenge und enthält nur die gemeinsamen Elemente
differenz = set2.difference(set1)  # -> gibt die Differenz zwischen 2 sets zurück

print(differenz)

# Aufgabe 1
# Füge mit der `add()` Methode ein weiteres Tier, z.B. "Elefant", hinzu
tiere = {"Hund", "Katze", "Vogel"}

# Aufgabe 2
# Entferne die Zahl 3 mit der `remove()` Methode
zahlen = {1, 2, 3, 4, 5}

# Aufgabe 3
# Verwende `discard()` für die Farbe "blau" und gib dein set aus
farben = {"rot", "gelb", "grün", "schwarz", "weiß"}

# Aufgabe 4
# Verwende `union()`, um ein Set mit allen Früchten und Gemüsen zu erstellen und gib es aus
obst = {"Apfel", "Banane", "Kirsche", "Pflaume", "Mango"}
gemüse = {"Karotte", "Tomate", "Salat", "Brokkoli", "Kartoffel"}

# Aufgabe 5
# Verwende `intersection()` für die gemeinsamen Städte heruaszufiltern und gib sie aus
staedte = {"Berlin", "Hamburg", "München", "Köln", "Stuttgart"}
staedte2 = {"München", "Düsseldorf", "Berlin", "Leipzig"}

# Aufgabe 6
# Verwende `difference()`, um die Sportarten zu finden, die nur in deinem Lieblings-Set sind
sportarten_studio1 = {"Fußball", "Basketball", "Tennis"}
sportarten_studio2 = {"Tennis", "Golf", "Schwimmen"}

# Aufgabe 7
# Finde die Tiere, die nur in einem der beiden Gehege vorkommen (nicht in beiden).

gehege_1 = {"Löwe", "Tiger", "Elefant", "Zebra"}
gehege_2 = {"Tiger", "Elefant", "Giraffe", "Nashorn"}

print(gehege_1 ^ gehege_2)
print(gehege_1.symmetric_difference(gehege_2))
