import random
random.seed()

def leicht():
    faktor = random.randint(-10, 10)
    n = 0
    while n == 0:
        n = random.randint(-10, 10)
    z = faktor * n
    print(f"Ganze Zahl berechnen: {z}/{n}")
    input()
    print("Ergebnes:", faktor)