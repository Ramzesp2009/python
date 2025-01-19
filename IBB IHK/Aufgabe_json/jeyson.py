import json

# JSON Daten lesen
""" def read_json():
    with open("test.json", "r") as file:
        content = json.load(file)

        for entry in content:
            print(f" {entry["name"]} ist {entry["alter"]}")

read_json() """

# 1. Datei lesen
# 2. Neue Daten definieren
# 3. leere Liste definieren und Daten in der leeren Liste speichern
# 4. JSON lesen und Datein in leere Liste speichern
# 5. Neuen Datensatz an die Liste anhängen
# 6. Neuen Datensatz mit json.dump() speichern


# new_data = {
#     "name": "Mucki",
#     "nachname": "Igel",
#     "alter": 1
# }
#
#
# def save_data():
#     users = []
#     with open("test.json", "r") as file:
#         data = json.load(file)
#         users = data
#     users.append(new_data)
#
#     with open("test.json", "w") as file:
#         json.dump(users, file)
#
#
# save_data()