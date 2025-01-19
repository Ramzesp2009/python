class Dog:
    # Atribut of the slass
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} year old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

brus = JackRussellTerrier("Brus", 10)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
maili = GoldenRetriever("Maili", 6)

print(brus)
print(brus.speak())
print(maili.speak())
print(jack)
print(jim.speak("Woof"))

print(type(brus))

print(isinstance(brus, Dog))


