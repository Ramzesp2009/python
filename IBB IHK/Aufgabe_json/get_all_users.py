import json


def get_all_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Die Datei users.json wurde nicht gefunden.")
        return []
