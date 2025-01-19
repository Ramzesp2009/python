# Aufgabe 6
# Erstelle eine Basisklasse Bankkonto mit Kontonummer und
# kontostand als Attribute Erstelle darin die Methoden
# einzahlen(betrag) und auszahlen(betrag)
# 6.2
# Erstelle die Subklasse Sparkonto mit einem Attribut
# zins_satz und einer Methode zinsen_hinzufügen
# Erstelle die Subklasse Girokonto, welches einen
# Dispo-Kreditrahmen besitzt und auszahlen(betrag) entsprechend anpasst
# Simuliere mit diesen Klassen eine Bank, indem du
# mehrere Konten erstellst und Transaktionen durchführst.


class BankKonto:
    def __init__(self, kontonummer, kontostand=0):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            return f"Auf der Konto hat {betrag}€ eingezahlt. Der Kontostand ist {self.kontostand}€"
        else:
            return "Der Betrag muss positiv sein."


    def auszahlen(self, betrag):
        if 0 < betrag <= self.kontostand:
            return f"Aus der Konto hat {betrag}€ abgehoben"
        else:
            return "Nicht genugend Guthaben oder ungultiger Betrag"


class SparKonto(BankKonto):
    def __init__(self, kontonummer, kontostand, zins_satz):
        super().__init__(kontonummer, kontostand)
        self.zins_satz = zins_satz

    def zinsen_hinzufügen(self):
        zinsen = self.kontostand * self.zins_satz
        self.kontostand +=zinsen
        return (f"Zinsen in Hohe von {zinsen}€ wurden hinzugefugt."
                f"Neue Kontostand: {self.kontostand}€")


class GiroKonto(BankKonto):
    def __init__(self, kontonummer, kontostand=0, dispo_kreditrahmen=500):
        super().__init__(kontonummer, kontostand)
        self.dispo_kreditrahmen = dispo_kreditrahmen

    def auszahlen(self, betrag):
        if betrag > 0 and (self.kontostand - betrag) >= -self.dispo_kreditrahmen:
            self.kontostand -= betrag
            return f"{betrag}€ wurden ausgezahlt. Neuer Kontostand: {self.kontostand}€"
        else:
            return ("Auszahlung fehlgeschlagen. Kreditrahmen uberschritten "
                    "oder ungultiger Betrag")


def main():
    sparkonto = SparKonto(kontonummer="1001", kontostand=1000, zins_satz=0.03)
    girokonto = GiroKonto(kontonummer="2001", kontostand=500, dispo_kreditrahmen=1000)

    # Transaktionen durchführen
    print("\nSparkonto Transaktionen:")
    print(sparkonto.einzahlen(200))
    print(sparkonto.zinsen_hinzufügen())
    print(sparkonto.auszahlen(500))

    print("\nGirokonto Transaktionen:")
    print(girokonto.einzahlen(300))
    print(girokonto.auszahlen(1000))
    print(girokonto.auszahlen(800))

if __name__ == '__main__':
    main()