class Buch:
    def __init__(self, title: str):
        self._title = title

    def get_title(self):
        return self._title


buch = Buch("Mark Iden")
print(buch.get_title())