import random
random.seed()

x = "Paris"
print("Wert =", x)

match x:
    case "Paris":
        print("Frankreich")
    case "Rom":
        print("Italien")
    case "Madrid":
        print("Spanien")
    case _:
        print("Unbekannetes Land")
print()

x = random.randint(1, 6)
print("Wert =", x)

match x:
    case 1 | 3 | 5:
        print("ungerade")
    case 2 | 4 | 6:
        print("gerade")
    case _:
        print("Kein Wurfelwert")
print()

x = random.randint(1, 10) * 1.5
print("Wert =", x)

match x:
    case x if x < 5:
        print("kleiner Wert")
    case x if x > 11:
        print("groser Wert")
    case _:
        print("mittlerer Wert")
print()
