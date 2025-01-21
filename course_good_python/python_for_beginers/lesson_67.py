from typing import Callable

lst: list[int] = [1, 2, 3, 'start']

tpl: tuple[int]

elem: tuple[float, ...]
elem = (1.1, 1.2)

words: dict[str, int]
words = {'word': 1}

persons: set[str] = {'asd', 'lkj', 'wer'}

def get_positive(digits: list[int]) -> list[int]:
    return  list(filter(lambda x: x > 0, digits))


def get_digits(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))


def even(x: int) -> bool:
    return bool(x % 2 == 0)


print(get_digits(even, [1, 2, 3, 4, 5, 6, 7]))
