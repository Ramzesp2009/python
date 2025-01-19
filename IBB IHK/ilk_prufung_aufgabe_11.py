# Angenommen, der folgende Code wird fehlerfrei ausgeführt:
import random

v1 = random.random
v2 = random.random

# Welche der folgenden Ausdrücke wird immer als wahr ausgewertet?
# Tipp: Nehmen Sie an, dass random.choice() zufällig einen Wert aus der übergebenen Liste auswählt.

# len(random.sample([1,2,3],2)) > 2   Richtig bei ILK
# v1 == v2
# random.choice([1,2,3]) > 0   Richtig bei ILK
# v1

print(len(random.sample([1,2,3],2)) > 2)
print(v1 == v2)
print(random.choice([1,2,3]) > 0)
print(bool(v1))