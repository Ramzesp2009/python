import hashlib

def hash_password(password):
    """
    Berechnet den SHA-256-Hash eines gegebenen Passworts.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    # Vordefiniertes Passwort und dessen SHA-256-Hash
    gespeicherter_hash = hash_password("geheim")
    # print(gespeicherter_hash)
    # Benutzereingabe
    benutzer_eingabe = input("Bitte geben Sie Ihr Passwort ein: ")
    benutzer_hash = hash_password(benutzer_eingabe)
    # print(benutzer_hash)
    print(hashlib.algorithms_available)
    # Vergleich der Hashwerte
    if benutzer_hash == gespeicherter_hash:
        print("Login erfolgreich")
    else:
        print("Passwort ist falsch")

if __name__ == "__main__":
    main()
