import matplotlib.pyplot as plt
import matplotlib.markers as markers
import csv
from sys import argv


# die veir verfugbaren Features und ihre Spalten
feature_mapping = {
    0: "Sepal length",
    1: "Sepal width",
    2: "Petal length",
    3: "Petal width"
}

# Frben und Formen, die fur die Spezies verwendet werden sollen
color_mapping = {
    "Iris-setora": "red",
    "Iris-versicolor": "green",
    "Iris-virginica": "blue"
}
marker_mapping = {
    "Iris-setora": 'o',
    "Iris-versicolor": 'v',
    "Iris-virginica": '*'
}

# CSV-Daten einlesen
irises = []
iris_file = open("iris.csv", 'r')
for line in csv.reader(iris_file):
    irises.append(line)
iris_file.close()

# Vorgabe: X = sepal width, Y = sepal length
x_feature = 0
y_feature = 1

# Wurden zwei verschiedene erlaubte Features als Argumente ubergeben?
possible_features = ['0', '1', '2', '3']
if (len(argv) >= 3 and argv[1]  in possible_features
    and argv[2] in possible_features and argv[1] != argv[2]):
    x_feature = int(argv[1])
    y_feature = int(argv[2])

# plot_values: je eine zweidimensionale Liste fur alle Punkte eiver Spezies
plot_values = {}
for iris in irises:
    if iris[4] not in plot_values:
        plot_values[iris[4]] = [[], []]
        plot_values[iris[4]][0].append(float(iris[x_feature]))
        plot_values[iris[4]][1].append(float(iris[y_feature]))

# Die eigentliche Zeichnung erstellen.
plt.title(f"{feature_mapping[x_feature]} and "
          f"{feature_mapping[y_feature]} of iris flowers")
plt.xlabel(feature_mapping[x_feature])
plt.ylabel(feature_mapping[y_feature])
for species in plot_values.keys():
    plt.scatter(
        plot_values[species][0],
        plot_values[species][1],
        color=color_mapping[species],
        marker=marker_mapping[species]
    )
plt.show()