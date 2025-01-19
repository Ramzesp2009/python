class Sicherheitssystem:
    def __init__(self, passwort: str):
        self.code = None
        self.__passwort = int(passwort)

    # def set_passwort(self):
    #     self.passwort = input("Enter set the password:\t")

    def __authentifizieren(self, code):
        if self.__passwort == code:
            print("Zugang erlaubt")
        else:
            print("Zugang nicht erlaubt")

    def zugang_gewahren(self):
        self.code = int(input("Please enter code:\t"))
        self.__authentifizieren(self.code)



sicher = Sicherheitssystem('1234')
sicher.zugang_gewahren()