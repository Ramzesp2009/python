import random


class Planet:
    MAX_POPULATION = 20

    def __init__(self, name: str ) -> None:
        self.name = name
        self.population = 0
        self.food = random.randint(300, 2000)
        self.holz = random.randint(1500, 2000)
        self.stein = random.randint(1500, 2000)
        self.gold = 200
        self.humans = []
        self.gebaude = []

    def resourse_uberprufen(self, gebaude):
        return (
            self.food >= gebaude["food_costs"] and
            self.stein >= gebaude["stone_costs"] and
            self.holz >= gebaude["wood_costs"] and
            self.gold >= gebaude["gold_costs"]
        )

    def bauen(self, gebaude):
        if not self.resourse_uberprufen(gebaude):
            print("Nicht genugend Ressoursen fur dieses Gebaude!")
            return False
        self.food -= gebaude["food_costs"]
        self.stein -= gebaude["stone_costs"]
        self.holz -= gebaude["wood_costs"]
        self.gold -= gebaude["gold_costs"]
        self.gebaude.append(gebaude["name"])
        print(f"Gebaude {gebaude["name"]} wurde erfolgreich gebaut!")
        return True

    def add_human(self, human):
        if self.population < Planet.MAX_POPULATION:
            if self.food >= 100:
                self.humans.append(human)
                self.population += 1
                self.food -= 100
                print(f"Der Mensch {human.name} wurde hinzugefugt.")
            else:
                print("Nicht genug Nahrung")
        else:
            print("Maximale Bevolkerung erreicht.")

    def __str__(self) -> str:
        return (f"Der Name des Planets - {self.name}, "
                f"Bevolkerungszahl - {self.population}, "
                f"Nahrung - {self.food}, "
                f"Holz - {self.holz}, "
                f"Stein - {self.stein}, "
                f"Gold - {self.gold}")
