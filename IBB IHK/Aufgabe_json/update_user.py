import json


def update_user(users):
    name = input("Name des Mitglieds, das bearbeitet werden soll: ")
    for user in users:
        if user["name"].lower() == name.lower():
            print("Mitglied gefunden. Gib neue Werte ein"
                  "(leer lassen, um den alten Wert zu behandeln):")
            new_name = input(f"Neuer Name ({user['name']}): ") or user["name"]
            new_alter = input(f"Neues Alter ({user['alter']}): ") or user["alter"]
            new_email = input(f"Neue Email ({user['email']}): ") or user["email"]
            new_hobby = input(f"Neues Hobby({user['hobby']}): ") or user["hobby"]

            user.update({"name": new_name, "alter": new_alter,
                         "email": new_email, "hobby": new_hobby})

            try:
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                print(f"Mitglied {name} wurde aktualisiert.")
            except Exception as e:
                print(f"Fehler beim Speichern: {e}")
            return
    print("Mitglied nicht gefunden.")
