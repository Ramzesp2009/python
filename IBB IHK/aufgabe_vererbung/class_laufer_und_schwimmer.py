# Aufgabe 4
# Erstelle die Klasse Läufer und Schwimmer, jede mit einer Methode,
# die ihre Fähigkeit beschreibt (laufen und schwimmen)
# Erstelle eine Klasse Triathlet, die von beiden Klassen erbt und
# alle Fähigkeiten vereint.
# Teste den Zugriff auf die geerbten Methoden
# Erweitere die Klasse Triathlet um die Methode Radfahren.


class Laufer:
    def __init__(self):
        pass

    def laufen(self):
        return "Ich laufe"


class Schwimmer:
    def __init__(self):
        pass

    def schwimmen(self):
        return "Ich schwimme"


class Triathlet(Laufer, Schwimmer):
    def __init__(self):
        Laufer().__init__()
        Schwimmer().__init__()

    def radfahren(self):
        return "Ich fahre mit den Fahrrad"


def main():
    laufer = Laufer()
    print(laufer.laufen())

    schwimmer = Schwimmer()
    print(schwimmer.schwimmen())

    triathlet = Triathlet()
    print(triathlet.radfahren())
    print(triathlet.laufen())
    print(triathlet.schwimmen())


if __name__ == "__main__":
    main()