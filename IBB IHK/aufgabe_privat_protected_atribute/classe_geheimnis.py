class Geheimnis:
    def __init__(self):
        self.__geheimnis = 'some secret'

    def get_geheimnis(self):
        return self.__geheimnis



geheimnis = Geheimnis()
print(geheimnis.get_geheimnis())