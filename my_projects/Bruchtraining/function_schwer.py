# Schwer Funktion
from random import *

from my_projects.Bruchtraining.function_mittel import produkt, ausgabe

ops = '+', '-', '*', '/'

def schwer():
    az = produkt(2)
    an = produkt(2)
    bz = produkt(2)
    bn = produkt(2)
    op = random.choice(ops)
    print(f"Ergebnisbruch berechnen: {az}/{an} {op} {bz}/{bn}")

    if op == "+":
        z = az * bn + az * bz
        n = an * bn
    elif op == "-":
        z = az * bn - az * bz
        n = an * bn
    elif op == "*":
        z = az * bz
        n = an * bn
    else:
        z = az * bn
        n = an * bz

    input()
    ausgabe()