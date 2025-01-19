# class Bankkonto:
#     def __init__(self, kontostand: float):
#         self.__kontostand = kontostand
#
#     def set_kontostand(self, neu_kontostand):
#         self.__kontostand += neu_kontostand
#
#     def get_kontostand(self):
#         return self.__kontostand
#
#
#
# bankkonto = Bankkonto(5000)
# print(bankkonto.get_kontostand())
# bankkonto.set_kontostand(500)
# print(bankkonto.get_kontostand())


class Bankkonto:
    def __init__(self, kontonr, kontostand):
        self.kontonr = kontonr
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def auszahlen(self, betrag):
        self.kontostand -= betrag

    def kontostand_ausgeben(self):
        return f"Konto {self.kontonr} hat einen Kontostand von: {self.kontostand} €"


class Sparkonto(Bankkonto):
    def __init__(self, kontonr, kontostand, zins_satz):
        super().__init__(kontonr, kontostand)
        self.zins_satz = zins_satz

    def zinsen_hinzufügen(self):
        self.kontostand += float(self.kontostand) * (self.zins_satz / 100)


class GiroKonto(Bankkonto):
    dispo = -3000

    def __init__(self, kontonr, kontostand):
        super().__init__(kontonr, kontostand)

    def auszahlen(self, betrag):
        if (self.kontostand - betrag) < self.dispo:
            return "Auszahlung nicht möglich! Zu hoher Betrag"
        else:
            return super().auszahlen(betrag)


k1 = GiroKonto("12345", 2000)
print(k1.kontostand_ausgeben())
k1.auszahlen(500)
print(k1.kontostand_ausgeben())
print()
k2 = Sparkonto("23456", 10000, 5)
print(k2.kontostand_ausgeben())
k2.zinsen_hinzufügen()
print(k2.kontostand_ausgeben())
print()
k3 = Bankkonto("34567", 1000)
k3.einzahlen(200)
print(k3.kontostand_ausgeben())
k3.auszahlen(500)
print(k3.kontostand_ausgeben())
