class Mitarbeiter:
    def __init__(self, name, abteilung, gehalt):
        self.name = name
        self._abteilung = abteilung
        self.__gehalt = gehalt

    def set_gehalt(self, other):
        self.__gehalt += other

    def get_gehalt(self):
        return self.__gehalt



mitarbeiter = Mitarbeiter('Pavlo', 'Programmer', 5000)
print(mitarbeiter.name)
print(mitarbeiter._abteilung)
print(mitarbeiter.get_gehalt())