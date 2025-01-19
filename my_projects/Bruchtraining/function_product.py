# Function Product
from random import random

from pythonbuch_beispiele.bruchtraining import prob


def produkt(anzahl):
    wert = 1
    for i in range(anzahl):
        wert *= random.choice(prob)
    if random.randint(0, 1) == 0:
        return wert
    else:
        return -wert
