from planet import Planet
from human import Human
import time
from gebaude import Gebaude


class Hauptmenu:
    def __init__(self):
        self.planet_list = []

    def show_menu(self):
        while True:
            print("\nHauptmenu:")
            print("1: Neuen Planet erstellen")
            print("2: Menschen erschaffen")
            print("3: Gebaude bauen")
            print("4: Programm beenden")
            auswahl = input('- ')

            if auswahl == '1':
                self.create_planet()
            elif auswahl == '2':
                self.create_human()
            elif auswahl == '3':
                self.gebaude_bauen()
            elif auswahl == '4':
                print("Programm beendet")
                break
            else:
                print("Ungultige Eingabe.")
                time.sleep(1)

    def create_planet(self):
        name = input("Gib den Namen des neuen Planeten ein: ")
        new_planet = Planet(name)
        self.planet_list.append(new_planet)
        print(f"Der neue Planet {name} wurde erstellt.")
        time.sleep(1)

    def create_human(self):
        if not self.planet_list:
            print("Es gibt keine Planeten zu denen Sie Menschen "
                  "hinzufugen konnen.")
            time.sleep(1)
            return
        self.show_planets()
        planet_index = int(input("Wahle einen Planeten aus (Index): ")) - 1
        if 0 <= planet_index < len(self.planet_list):
            planet = self.planet_list[planet_index]
            name: str = input("Geben Sie den Namen des neuen Menschen ein: ")
            alter: int = int(input("Geben Sie Alter des Menschen ein: "))
            beruf: str = input("Geben Sie den Beruf des Menschen ein: ")
            human = Human(name=name, alter=alter, job=beruf)
            planet.add_human(human)
        else:
            print("Ungulige Wahl.")
            time.sleep(1)

    def show_planets(self):
        print("Planeten: ")
        for i, planet in enumerate(self.planet_list, 1):
            print(f"{i}: {planet.name}")

    def gebaude_bauen(self):
        if not self.planet_list:
            print("Es gibt keine Planeten, auf denen Sie ein Gabaude bauen konnen.")
            time.sleep(1)
            return
        self.show_planets()
        planet_index = int(input("Wahlen Sie einen Planeten aus (Index): ")) - 1
        if 0 <= planet_index < len(self.planet_list):
            planet = self.planet_list[planet_index]
            print("Verfugbare Gebaude:")
            for i, gebaude in enumerate(Gebaude.vorhandende_gebaude, 1):
                print(f"{i}: {gebaude['name']} - Nahrung: {gebaude['food_costs']}, "
                      f"Stein: {gebaude['stone_costs']}, Holz: {gebaude['wood_costs']},"
                      f"Gold: {gebaude['gold_costs']}")
            gebaude_index = int(input("Wahlen Sie ein Gaboude aus (Index): ")) - 1
            if 0 <= gebaude_index < len(Gebaude.vorhandende_gebaude):
                gebaude = Gebaude.vorhandende_gebaude[gebaude_index]
                if gebaude['name'] == 'Rathaus' or 'Rathaus' in planet.gebaude:
                    planet.bauen(gebaude)
                else:
                    print("Sie mussen zuerst ein Rathaus bauen!")
            else:
                print("Ungultige Wahl.")
        else:
            print("Ungultige Planet.")
        time.sleep(1)

menu = Hauptmenu()
menu.show_menu()
