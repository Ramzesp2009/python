# Ausgabe Function
import math


def ausgabe(z, n):
    ggT = math.gcd(z, n)
    z = int(z / ggT)
    n = int(n / ggT)
    if n < 0:
        z *= -1
        n *= -1
    print("Ergebnis:", z if n == 1 else f"{z}/{n}")

