class Human:
    def __init__(self, name: str, alter: int, job: str) -> None:
        self.name = name
        self.alter = alter
        self.job = job

    def __str__(self):
        return (f"Name des Mensch {self.name},"
                f"Alter des Mensch {self.alter},"
                f"Beruf des Mensch {self.job}")
