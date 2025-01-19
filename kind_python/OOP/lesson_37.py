from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = []

    def __repr__(self):
        return f"Thing name={self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)
    # dims: list = []

    def __eq__(self, other):
        return self.weight == other.weight


td = ThingData("book", 100)
td2 = ThingData("book", 100)
td.dims.append(10)
print(td)
print(td2)