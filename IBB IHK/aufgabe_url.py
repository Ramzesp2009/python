import requests
import random
import json
from datetime import datetime

# Aufgabe 1
# Verwendet folgende API um einen zufälligen Charakter aus einem Fantasy Spiel zu generieren:
#  https://www.dnd5eapi.co/api/races


def generate_random_fantasy_character():
    api_url = "https://www.dnd5eapi.co/api/races"

    try:
        # API-Anfrage senden
        response = requests.get(api_url)
        response.raise_for_status()  # Fehler überprüfen

        # Daten aus der API lesen
        races_data = response.json()
        races = races_data['results']

        # Zufällige Rasse auswählen
        random_race = random.choice(races)

        # Details zur ausgewählten Rasse abrufen
        race_details_url = f"https://www.dnd5eapi.co{random_race['url']}"
        race_response = requests.get(race_details_url)
        race_response.raise_for_status()
        race_details = race_response.json()

        # Charakter anzeigen
        print("🎲 Zufälliger Charakter:")
        print(f"Rasse: {race_details['name']}")
        print(f"Beschreibung: {race_details.get('alignment', 'Keine Beschreibung verfügbar')}")
        print(f"Sprachen: {', '.join(lang['name'] for lang in race_details.get('languages', []))}")

    except requests.exceptions.RequestException as e:
        print("Fehler bei der API-Anfrage:", e)


# Funktion aufrufen
generate_random_fantasy_character()
print('\n')
# Aufgabe 2
# Verwende folgende API um dem Charakter eine zufällige Charakterklasse zuzuordnen
#  https://www.dnd5eapi.co/api/classes


def generate_random_fantasy_character():
    # URL für die Rassen und Klassen
    races_api_url = "https://www.dnd5eapi.co/api/races"
    classes_api_url = "https://www.dnd5eapi.co/api/classes"

    try:
        # API-Anfrage für Rassen senden
        response_races = requests.get(races_api_url)
        response_races.raise_for_status()  # Fehler überprüfen
        races_data = response_races.json()
        races = races_data['results']

        # API-Anfrage für Klassen senden
        response_classes = requests.get(classes_api_url)
        response_classes.raise_for_status()  # Fehler überprüfen
        classes_data = response_classes.json()
        classes = classes_data['results']

        # Zufällige Rasse und Klasse auswählen
        random_race = random.choice(races)
        random_class = random.choice(classes)

        # Details zur zufälligen Rasse abrufen
        race_details_url = f"https://www.dnd5eapi.co{random_race['url']}"
        response_race_details = requests.get(race_details_url)
        response_race_details.raise_for_status()
        race_details = response_race_details.json()

        # Details zur zufälligen Klasse abrufen
        class_details_url = f"https://www.dnd5eapi.co{random_class['url']}"
        response_class_details = requests.get(class_details_url)
        response_class_details.raise_for_status()
        class_details = response_class_details.json()

        # Charakter ausgeben
        print("🎲 Zufälliger Charakter:")
        print(f"Rasse: {race_details['name']}")
        print(f"Beschreibung: {race_details.get('alignment', 'Keine Beschreibung verfügbar')}")
        print(f"Sprachen: {', '.join(lang['name'] for lang in race_details.get('languages', []))}")
        print(f"Klasse: {class_details['name']}")
        print(f"Klassenbeschreibung: {class_details.get('hit_die', 'Keine Beschreibung verfügbar')}")

    except requests.exceptions.RequestException as e:
        print("Fehler bei der API-Anfrage:", e)


# Funktion aufrufen
generate_random_fantasy_character()
print('\n')

# Aufgabe 3
# Generiert zufällige Werte für die Charakterattribute Stärke, Intelligenz, Agilität als Dictionary von 1 bis 50


def generate_character_attributes():
    # Zufällige Werte für Attribute im Bereich von 1 bis 50
    attributes = {
        "Stärke": random.randint(1, 50),
        "Intelligenz": random.randint(1, 50),
        "Agilität": random.randint(1, 50),
    }

    return attributes


# Zufällige Attribute generieren
character_attributes = generate_character_attributes()

# Ausgabe der Attribute
print("🎲 Zufällige Charakterattribute:")
for attribute, value in character_attributes.items():
    print(f"{attribute}: {value}")
print('\n')

# Aufgabe 4
# Speichert euren erstellten Character in einer json Datei und erstellt einen timestamp mit der
# Library datetime, welcher auch in der json Datei gespeichert wird und angibt, wann der
# Charakter erstellt wurde.




def generate_random_fantasy_character():
    # URL für die Rassen und Klassen
    races_api_url = "https://www.dnd5eapi.co/api/races"
    classes_api_url = "https://www.dnd5eapi.co/api/classes"

    try:
        # API-Anfrage für Rassen senden
        response_races = requests.get(races_api_url)
        response_races.raise_for_status()  # Fehler überprüfen
        races_data = response_races.json()
        races = races_data['results']

        # API-Anfrage für Klassen senden
        response_classes = requests.get(classes_api_url)
        response_classes.raise_for_status()  # Fehler überprüfen
        classes_data = response_classes.json()
        classes = classes_data['results']

        # Zufällige Rasse und Klasse auswählen
        random_race = random.choice(races)
        random_class = random.choice(classes)

        # Details zur zufälligen Rasse abrufen
        race_details_url = f"https://www.dnd5eapi.co{random_race['url']}"
        response_race_details = requests.get(race_details_url)
        response_race_details.raise_for_status()
        race_details = response_race_details.json()

        # Details zur zufälligen Klasse abrufen
        class_details_url = f"https://www.dnd5eapi.co{random_class['url']}"
        response_class_details = requests.get(class_details_url)
        response_class_details.raise_for_status()
        class_details = response_class_details.json()

        # Zufällige Werte für Attribute generieren
        attributes = {
            "Stärke": random.randint(1, 50),
            "Intelligenz": random.randint(1, 50),
            "Agilität": random.randint(1, 50),
        }

        # Erstellungszeitpunkt (Timestamp)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Charakterdaten als Dictionary
        character = {
            "name": "Charakter_" + str(random.randint(1000, 9999)),
            "race": race_details['name'],
            "class": class_details['name'],
            "attributes": attributes,
            "timestamp": timestamp,
        }

        # Speichern des Charakters in einer JSON-Datei
        with open("character.json", "w") as json_file:
            json.dump(character, json_file, indent=4)

        print("🎲 Charakter wurde erstellt und gespeichert:")
        for key, value in character.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print("Fehler bei der API-Anfrage:", e)



# Funktion aufrufen
generate_random_fantasy_character()
print('\n')

# Aufgabe 5
# Als nächstes wollt ihr mehrere Charaktere in eurer json
# Datei speichern. Also los gehts! :)


def generate_random_fantasy_character():
    # URL für die Rassen und Klassen
    races_api_url = "https://www.dnd5eapi.co/api/races"
    classes_api_url = "https://www.dnd5eapi.co/api/classes"

    try:
        # API-Anfrage für Rassen senden
        response_races = requests.get(races_api_url)
        response_races.raise_for_status()  # Fehler überprüfen
        races_data = response_races.json()
        races = races_data['results']

        # API-Anfrage für Klassen senden
        response_classes = requests.get(classes_api_url)
        response_classes.raise_for_status()  # Fehler überprüfen
        classes_data = response_classes.json()
        classes = classes_data['results']

        # Zufällige Rasse und Klasse auswählen
        random_race = random.choice(races)
        random_class = random.choice(classes)

        # Details zur zufälligen Rasse abrufen
        race_details_url = f"https://www.dnd5eapi.co{random_race['url']}"
        response_race_details = requests.get(race_details_url)
        response_race_details.raise_for_status()
        race_details = response_race_details.json()

        # Details zur zufälligen Klasse abrufen
        class_details_url = f"https://www.dnd5eapi.co{random_class['url']}"
        response_class_details = requests.get(class_details_url)
        response_class_details.raise_for_status()
        class_details = response_class_details.json()

        # Zufällige Werte für Attribute generieren
        attributes = {
            "Stärke": random.randint(1, 50),
            "Intelligenz": random.randint(1, 50),
            "Agilität": random.randint(1, 50),
        }

        # Erstellungszeitpunkt (Timestamp)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Charakterdaten als Dictionary
        character = {
            "name": "Charakter_" + str(random.randint(1000, 9999)),
            "race": race_details['name'],
            "class": class_details['name'],
            "attributes": attributes,
            "timestamp": timestamp,
        }

        return character

    except requests.exceptions.RequestException as e:
        print("Fehler bei der API-Anfrage:", e)
        return None


def save_characters_to_json(character_list):
    # Wenn die Datei existiert, laden wir die existierenden Charaktere
    try:
        with open("characters.json", "r") as file:
            existing_characters = json.load(file)
    except FileNotFoundError:
        existing_characters = []

    # Füge die neuen Charaktere zu den bestehenden hinzu
    existing_characters.extend(character_list)

    # Speichere die aktualisierte Liste in der JSON-Datei
    with open("characters.json", "w") as file:
        json.dump(existing_characters, file, indent=4)


def generate_multiple_characters(num_characters):
    characters = []
    for _ in range(num_characters):
        character = generate_random_fantasy_character()
        if character:
            characters.append(character)
    for i in characters:
        print(i)
    # Speichere die Charaktere in der JSON-Datei
    save_characters_to_json(characters)
    print(f"{num_characters} Charaktere wurden erfolgreich erstellt und gespeichert.")


# Beispiel: Erstelle 5 zufällige Charaktere
generate_multiple_characters(5)
