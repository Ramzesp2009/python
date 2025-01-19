from typing import List


def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    """
    Berechnet die Skyline aus einer Liste von Gebäuden mit allen Höhenänderungspunkten.

    Args:
        buildings: Liste von Gebäuden, wobei jedes Gebäude als [left, right, height] definiert ist

    Returns:
        Liste von allen Punkten der Skyline als [x, height], einschließlich horizontaler Linien
    """
    # Erstelle Events für Start und Ende jedes Gebäudes
    events = []
    for left, right, height in buildings:
        # Füge Start-Events hinzu
        events.append((left, height, 1))  # 1 für Start
        # Füge End-Events hinzu
        events.append((right, height, -1))  # -1 für Ende

    # Sortiere Events nach x-Koordinate
    events.sort()

    # Initialisiere Ergebnis-Liste und aktive Höhen
    skyline = []
    active_heights = {0}  # Menge der aktiven Höhen, startet mit Grundhöhe 0
    current_height = 0

    # Verarbeite alle Events
    for x, height, event_type in events:
        # Füge vorherige Höhe hinzu
        if skyline and skyline[-1][0] != x:
            skyline.append([x, current_height])

        if event_type == 1:  # Start-Event
            active_heights.add(height)
        else:  # End-Event
            active_heights.remove(height)

        # Neue maximale Höhe
        new_height = max(active_heights)

        # Füge neuen Punkt hinzu
        skyline.append([x, new_height])
        current_height = new_height

    return skyline


# Beispiel zur Verwendung
def main():
    # Testbeispiel
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    result = get_skyline(buildings)
    print(f"Eingabe: {buildings}")
    print(f"Skyline: {result}")


if __name__ == "__main__":
    main()