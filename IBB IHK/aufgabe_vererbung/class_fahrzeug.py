# Aufgabe 1
# Erstelle eine Klasse Fahrzeug die folgende Instanzattribute und Methoden hat:
# - Instanzattribute: marke, farbe
# - Methode: beschreiben()
# Aufgabe 1.2
# Erstelle eine Subklasse Auto, die von Fahrzeug erbt
# füge das Attribut anzahl_tueren hinzu
# überschreibe die Methode beschreiben() um die Anzahl der Türen anzugeben
# Teste deine Instanzen von Fahrzeug und Instanzen


class Fahrzeug:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def beschreiben(self):
        return f"Der Fahrzeug {self.marke} hat die Farbe {self.farbe}"


class Auto(Fahrzeug):
    def __init__(self, marke, farbe, anzahl_tueren):
        super().__init__(marke, farbe)
        self.anzahl_tueren = anzahl_tueren

    def beschreiben(self):
        return f"Die Anzahl die Tueren ist {self.anzahl_tueren}"


bmw = Auto(marke='BMW', farbe='Black', anzahl_tueren=4)
print(bmw.beschreiben())
