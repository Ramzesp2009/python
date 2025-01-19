class Fahrzeug:
    def __init__(self, speed):
        self._geschwindigkeit = speed


class Sedan(Fahrzeug):
    def __init__(self, speed):
        super().__init__(speed)

    def speed_up(self, kmh):
        self._geschwindigkeit += kmh


sedan = Sedan(180)
sedan.speed_up(50)
print(sedan._geschwindigkeit)
