import json


def delete_user(users):
    name = input("Name des Mitglieds, das entfernt werden soll: ")
    for user in users:
        if user["name"].lower() == name.lower():
            users.remove(user)
            try:
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                print(f"Mitglied {name} wurde entfernt.")
            except Exception as e:
                print(f"Fehler beim Speichern: {e}")
            return
    print("Mitglied nicht gefunden.")
