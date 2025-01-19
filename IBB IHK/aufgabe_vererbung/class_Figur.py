# Aufgabe 5
# importiere ABC (Abstract Base Class) und abstractmethod
# aus dem Modul abc Erstelle eine abstrakte Klasse Figur
# mit einer abstrakten Methode flaeche() und einer normalen
# Methode beschreibung(), die "Das ist eine geometrische Figur" ausgibt
# 5.2
# Erstelle die Subklassen Kreis und Rechteck, die flaeche()
# implementieren und die jeweilige Fläche des Objekts berechnen.
# Gib die berechnete Fläche und die Beschreibung aus

from abc import ABC, abstractmethod
import math


class Figur(ABC):
    @abstractmethod
    def flaeche(self):
        pass

    def beschreibung(self):
        return "Das ist eine geometrische Figur"


class Kreis(Figur):
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return math.pi * (self.radius ** 2)

    def beschreibung(self):
        return "Die Klasse gibt die berechnete Flaeche des Kreises aus"

class Rechteck(Figur):
    def __init__(self, breit, hoch):
        self.breit = breit
        self.hoch = hoch

    def flaeche(self):
        return self.breit * self.hoch

    def beschreibung(self):
        return "Die Klasse gibt die berechnete Flaeche des Rechtecks aus"


def main():
    kreis = Kreis(5)
    kreis.beschreibung()
    print(f"Die Fläche des Kreises beträgt: {kreis.flaeche()}")
    print()

    rechteck = Rechteck(5, 4)
    rechteck.beschreibung()
    print(f"Die Fläche des Rechtecks beträgt: {rechteck.flaeche()}")


if __name__ == "__main__":
    main()