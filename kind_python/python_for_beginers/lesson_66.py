from typing import Union, Optional, Any, Final

MAX_VALUE: Final = 1000


Digit = Union[int, float]

Str = Optional[str]
StrType = Union[str, None]

def mul2(x: Digit, y: int | float) -> Union[int, float]:
    return x * y


MAX_VALUE = 200

print(MAX_VALUE)

def show_x(x: Any, descr: Optional[str] = None) -> None:
    if descr:
        print(f"{descr} {x}")
    else:
        print(f"x = {x}")


# res = mul2("sdtr")
# print(res)
# print(show_x.__annotations__)
show_x(55.44556, 444)