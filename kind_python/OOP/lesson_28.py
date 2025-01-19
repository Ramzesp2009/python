try:
    x, y = map(int, input('Enter two numbers: ').split())
    res = x / y
except ValueError:
    print('Error')
except Exception as e:
    print('error', e)
else:
    print(x / y)


print("The end of program")