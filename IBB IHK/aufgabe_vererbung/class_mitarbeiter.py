# Aufgabe 3
# Erstelle eine Klasse mit dem Namen Mitarbeiter und den Instanzattributen
# name und gehalt. Füge eine Methode arbeiten() hinzu die "Mitarbeiter arbeitet ausgibt"
# 3.2
# Erstelle eine Subklasse Manager die zusätzlich ein Attribut teamgroesse hat.
# Überschreibe die Methode arbeiten() in der Subklasse, sodass sie zusätzlich
# angibt, dass der Manager das Team leitet Verwende dabei super()


class Mitarbeiter:
    def __init__(self, name: str, gehalt: float):
        self.name = name
        self.gehalt = gehalt

    def arbeiten(self):
        print("Mitarbeiter arbeitet")


class Manager(Mitarbeiter):
    def __init__(self, name: str, gehalt: float, teamgrosse: int):
        super().__init__(name, gehalt)
        self.teamgrosse = teamgrosse

    def arbeiten(self):
        super().arbeiten()
        print("Manager leitet Team")


manager = Manager('Pavlo', '3000.0', 25)
manager.arbeiten()
