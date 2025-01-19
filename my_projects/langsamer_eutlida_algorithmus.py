import time


def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b

def test_nod(func):
    # Test 1
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("Test 1 - OK!")
    else:
        print("Test 1 - Fail")

    # Test 2
    a = 100
    b = 1
    res = func(a, b)
    if res == 7:
        print("Test 2 - OK!")
    else:
        print("Test 2 - Fail")

    # Test 3
    a = 2
    b = 10000000
    st = time.time()
    res = func(a, b)
    dt = time.time() - st
    if res == 2 and dt < 1:
        print(f"Test 3 - OK! Time = {dt}")
    else:
        print(f"Test 3 - Fail! Time = {dt}")

test_nod(get_nod)