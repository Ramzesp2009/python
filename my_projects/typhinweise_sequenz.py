def letztes(li):
    return li[-1]


print("String:", letztes("Guten Morgen"))
print("Tupel:", letztes((3, -14, 12)))
print("Liste:", letztes([7, 2, 16, -5, 53, 2]))


def letztes2[T](li: list[T]) -> T:
    return li[-1]


print("String:", letztes2('Guten Morgen'))
print("Tupel:", letztes2((3, -14, 12)))
print("Liste:", letztes2([7, 2, 16, -5, 53, 2]))
