import json


def save_user(users):
    name = input("Name: ")
    alter = input("Alter: ")
    email = input("Email: ")
    hobby = input("Hobby: ")

    new_user = {
        "name": name,
        "alter": alter,
        "email": email,
        "hobby": hobby
    }
    users.append(new_user)

    try:
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print(f"Mitglied {name} wurde hinzugefugt.")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
