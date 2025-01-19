class PasswortManager:
    def __init__(self, code, login):
        self.passwort = code
        self.user = login

    def get_passwort(self):
        antwort = input("Name des Benutzers:\t")
        if antwort == self.user:
            return f"Passwort ist -{self.passwort}-"
        else:
            return "Name des Benutzers ist falsch"



pasmanag = PasswortManager('Mycode', 'Pablo')
print(pasmanag.get_passwort())