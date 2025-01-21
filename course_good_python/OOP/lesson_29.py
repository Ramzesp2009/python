def get_values():
    try:
        x, y = map(int, input('Enter two numbers: ').split())
        return x, y
    except ValueError as v:
        print('ValueError', v)
        return  0, 0
    except Exception as e:
        print('error', e)
    finally:
        print("finally executed befor return")


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as z:
        print('ZeroDivisionError', z)
        return 0


res = 0
try:
    x, y = map(int, input('Enter two numbers: ').split())
    res = div(x, y)
except ValueError:
    print('Error')

print(res)