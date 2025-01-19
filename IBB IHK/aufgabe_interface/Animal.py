from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def get_name(self, name):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def get_name(self, name):
        print(f"My name is {name}")

    def make_sound(self):
        print("Wuff wuff")

class Cat(Animal):
    def get_name(self, name):
        print(f"My name is {name}")

    def make_sound(self):
        print("Mautz Mautz")


class Bird(Animal):
    def get_name(self, name):
        print(f"My name is {name}")

    def make_sound(self):
        print("Piep Piep Piep")


def treat_animal(animal: Animal, name: str):
    animal.get_name(name)
    animal.make_sound()


dog = Dog()
treat_animal(dog, 'Bruse')
