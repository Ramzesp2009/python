# Aufgabe 2
# Erstelle eine Basisklasse Tier mit den Instanzattributen name
# und art und einer Methode geraeusch_machen(), die "Das Tier macht
# ein Geräusch" ausgibt. Erstelle die Subklassen Hund, Katze, Maus, und Chinchilla
# Der Hund soll die Methode geraeusch_machen() überschreiben und WuffiWuff ausgeben.
# Die Katze soll "Ich bin Tom" ausgeben mit der Methode geraeusch_machen()
# Die Maus soll "Ich bin Jerry und ärgere Tom" ausgeben mit der Methode geraeusch_machen()
# Das Chinchilla soll ausgeben, was in der Klasse Tier in der Methode
# geraeusch_machen steht Musst du die Methode geraeusch_machen dafür überschreiben?

class Tier:
    def __init__(self, name, art):
        self.name = name
        self.art = art

    def geraeusch_machen(self):
        return "Das Tier macht ein Geräusch."

    def info(self):
        return f"Das Tier heisst {self.name}, hat die Rasse {self.art}"


class Hund(Tier):
    def __init__(self, name, art):
        super().__init__(name, art)

    def geraeusch_machen(self):
        return "WuffiWuff "

    def info(self):
        return f"Das Tier heisst {self.name}, hat die Rasse {self.art}"

class Katze(Tier):
    def __init__(self, name, art):
        super().__init__(name, art)

    def geraeusch_machen(self):
        return "Ich bin Tom"

    def info(self):
        return f"Das Tier heisst {self.name}, hat die Rasse {self.art}"


class Maus(Tier):
    def __init__(self, name, art):
        super().__init__(name, art)

    def geraeusch_machen(self):
        return "Ich bin Jerry und ärgere Tom"

    def info(self):
        return f"Das Tier heisst {self.name}, hat die Rasse {self.art}"


class Chinchilla(Tier):
    def __init__(self, name, art):
        super().__init__(name, art)

    def info(self):
        return f"Das Tier heisst {self.name}, hat die Rasse {self.art}"


hund = Hund('Reeks', 'Pitbull')
print(hund.geraeusch_machen())
print(hund.info())

katze = Katze('Tom', 'some_cat')
print(katze.geraeusch_machen())

maus = Maus('Jerry', 'some_mouse')
print(maus.geraeusch_machen())

chinchilla = Chinchilla('WTF', 'some_wtf')
print(chinchilla.geraeusch_machen())