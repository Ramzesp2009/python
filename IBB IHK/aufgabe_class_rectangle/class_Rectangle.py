class Ractangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return (self.width == other.width and
                self.height == other.height)





