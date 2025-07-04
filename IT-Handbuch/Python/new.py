import matplotlib.pyplot as plt
# import matplotlib.markers as markers # This import is not used
import csv
from sys import argv
from collections import defaultdict  # Useful for simplifying dictionary initialization

# die veir verfugbaren Features und ihre Spalten
feature_mapping = {
    0: "Sepal length",
    1: "Sepal width",
    2: "Petal length",
    3: "Petal width"
}

# Frben und Formen, die fur die Spezies verwendet werden sollen
color_mapping = {
    "Setosa": "red",  # Corrected "Iris-setora" to "Iris-setosa" if that's the species name in CSV
    "Versicolor": "green",
    "Virginica": "blue"
}
marker_mapping = {
    "Setosa": 'o',  # Corrected "Iris-setora" to "Iris-setosa"
    "Versicolor": 'v',
    "Virginica": '*'
}

# CSV-Daten einlesen
irises_data = []
try:
    with open("iris.csv", 'r') as iris_file:
        csv_reader = csv.reader(iris_file)
        header = next(csv_reader)  # Read and skip the header row
        for line in csv_reader:
            if len(line) >= 5:  # Ensure row has enough columns (species name is at index 4)
                irises_data.append(line)
            else:
                print(f"Warning: Skipping malformed row: {line}")
except FileNotFoundError:
    print("Error: iris.csv not found.")
    exit()
except StopIteration:
    print("Error: iris.csv is empty or contains only a header.")
    exit()

# Vorgabe: X = sepal width, Y = sepal length (Comment seems to mismatch default values)
# Default: x_feature = 0 (Sepal length), y_feature = 1 (Sepal width)
x_feature = 0
y_feature = 1

# Wurden zwei verschiedene erlaubte Features als Argumente ubergeben?
possible_feature_indices = [str(i) for i in feature_mapping.keys()]
if (len(argv) >= 3 and argv[1] in possible_feature_indices
        and argv[2] in possible_feature_indices and argv[1] != argv[2]):
    try:
        x_feature = int(argv[1])
        y_feature = int(argv[2])
    except ValueError:
        print("Error: Feature indices provided as arguments must be integers. Using defaults.")
        # Keep default x_feature, y_feature
else:
    if len(argv) > 1 and len(argv) < 3:
        print("Usage: python iris-scatter.py [x_feature_index y_feature_index]")
        print(f"Available feature indices: {list(feature_mapping.keys())}")
        print("Using default features.")
    elif len(argv) >= 3 and (argv[1] not in possible_feature_indices or \
                             argv[2] not in possible_feature_indices or \
                             argv[1] == argv[2]):
        print("Error: Invalid or duplicate feature indices provided.")
        print(f"Available feature indices: {list(feature_mapping.keys())}")
        print("Using default features.")

# plot_values: je eine zweidimensionale Liste fur alle Punkte einer Spezies
# Using defaultdict to simplify initialization: [[x_coords], [y_coords]]
plot_values = defaultdict(lambda: [[], []])

for iris_row in irises_data:
    # iris_row[4] should be the species name
    # iris_row[x_feature] and iris_row[y_feature] are the feature values
    try:
        species = iris_row[4]
        x_val = float(iris_row[x_feature])
        y_val = float(iris_row[y_feature])

        plot_values[species][0].append(x_val)
        plot_values[species][1].append(y_val)
    except IndexError:
        print(f"Warning: Row {iris_row} has insufficient data for selected features. Skipping.")
    except ValueError:
        # This might catch non-numeric data in feature columns if any survived filtering
        print(f"Warning: Could not convert data to float for row: {iris_row}. Skipping.")

# Die eigentliche Zeichnung erstellen.
if not plot_values:
    print("No data to plot. Check CSV file or feature selection.")
else:
    plt.title(f"{feature_mapping.get(x_feature, 'X-Feature')} vs "
              f"{feature_mapping.get(y_feature, 'Y-Feature')} of Iris Flowers")
    plt.xlabel(feature_mapping.get(x_feature, f"Feature {x_feature}"))
    plt.ylabel(feature_mapping.get(y_feature, f"Feature {y_feature}"))

    for species, data_lists in plot_values.items():
        if data_lists[0] and data_lists[1]:  # Ensure there are points to plot
            plt.scatter(
                data_lists[0],  # x values
                data_lists[1],  # y values
                color=color_mapping.get(species, 'gray'),  # Use .get() for robustness
                marker=marker_mapping.get(species, '.'),  # Use .get() for robustness
                label=species  # Add label for legend
            )
        else:
            print(f"No data points to plot for species: {species}")

    if any(plot_values.values()):  # Check if anything was actually plotted
        plt.legend()  # Add a legend
        plt.grid(True)  # Add a grid for better readability
        plt.show()
    else:
        print("No data was plotted.")
