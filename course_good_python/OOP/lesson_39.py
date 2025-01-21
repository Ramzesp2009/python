from dataclasses import dataclass, field, InitVar
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    # @staticmethod
    # def get_init_measure():
    #     return [0, 0, 0]

    def __post_init__(self):
        super().__post_init__()
        print("""Book: post_init""")


b = Book(1000, 100, "Python", "Romazan")
b2 = Book(1000, 100, "Python", "Romazan")
print(b)
print(b2)