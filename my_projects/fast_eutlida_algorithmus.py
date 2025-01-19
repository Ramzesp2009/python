import time


def get_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b  = b, a % b

    return a


def test_get_nod(func):
    st = time.time()
    a = 2
    b = 10000000
    res = func(a, b)
    t = time.time() - st
    if res == 6:
        print(f"Test 1 - OK! Time = {t}")
    else:
        print(f"Test 1 - Fail! Time = {t}")


test_get_nod(get_nod)