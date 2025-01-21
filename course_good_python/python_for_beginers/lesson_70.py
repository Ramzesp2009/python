from random import randint

cmd = ("Romazan", "Python", 199.99)
cmd = (1, "Romazan", "Deep Python_2", 399.99, 2022)

match cmd:
    case author, title, price:
        print(f"Book 1 {author}, {title}, {price}")
    case _, author, title, price, year:
        print(f"Book 2 {author}, {title}, {price}, {year}")
    case _:
        print("something else")



s = randint(1,5)

match s:
    case 1:
        print("Випало Один")
    case 2:
        print("Випало Два")
    case 3:
        print("Випало Три")
    case 4:
        print("Випало Чотири")
    case _:
        print("Ups!")