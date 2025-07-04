import matplotlib.pyplot as plt
import csv
import numpy as np
from sys import argv, exit

from sklearn.linear_model import LinearRegression

if len(argv) < 2:
    print(f"Verwendung: python3 {argv[0]} CSV-Datei [p]")
    exit(1)

# Datei importieren
filename = argv[1]
data = []
with open(filename, 'r') as data_file:
    reader = csv.reader(data_file)
    for line in reader:
        data.append([float(line[0]), float(line[1])])

# Koeffizienten der Geraden berechnen
# x = [row[0] for row in data]
# y = [row[1] for row in data]
# n = len(data)
# theta0 = (
#     (sum(y) * sum([xn**2 for xn in x]) - sum(x) * sum(
#     [xn * yn for xn, yn in zip(x, y)]
#     )) /
#     (n * sum([xn**2 for xn in x]) - sum(x)**2)
# )
# theta1 = (
#     (n * sum([xn * yn for xn, yn in zip(x, y)]) - sum(x) * sum(y)) /
#     (n * sum([xn**2 for xn in x]) - sum(x)**2)
# )
x = np.array([[row[0]] for row in data])
y = np.array([row[1] for row in data])
reg = LinearRegression().fit(x, y)
theta0 = reg.intercept_
theta1 = reg.coef_[0]



if len(argv) >=3 and argv[2] == 'p':
    # Modus Vorhersage
    print(f"Gefundene Geradengleichung: y = {theta0} + {theta1}x")
    print("Geben Sie x-Werte fur Prognosen ein; Q zum Beenden")
    while True:
        v_input = input(">")
        if v_input.lower() == 'q':
            break
        try:
            value = float(v_input)
            print(f"Prognose: {theta0 + theta1 * value}")
        except ValueError:
            print("Bitte nur Zahlen!")
else:
    # Modus Zeichnung
    plt.title(f"y = {theta0} + {theta1}x")
    plt.xlabel("Input data")
    plt.ylabel("Output data")
    plt.scatter(x, y, color='blue')
    xcoords = np.linspace(min(x), max(x), 100)
    ycoords = theta0 + theta1 * xcoords
    plt.plot(xcoords, ycoords, color='red')
    plt.show()