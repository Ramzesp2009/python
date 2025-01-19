# Aufgabe 1
# Erstelle eine Klasse mit dem Namen Planet und erstelle
# ein Klassenattribut mit einem Namen des Planeten

# Aufgabe 2
# Benutze in dieser Klasse eine magische Methode __str__()
# um dir den Namen des Planeten gut formatiert ausgeben zu können
# instanziere einen Planeten und gib ihn dir mit print aus


# Aufgabe 3
# baue einen Konstruktor, der bei dem instanzieren eines neuen
# Planeten aufgerufen wird und dem Planeten einen Namen gibt.
# Entferne das Klassenattribut name, weil du zukünftig das
# Instanzattribut verwenden wirst.

# Aufgabe 4
# schreibe in den Konstruktor weitere Instanzattribute
# population = 0 und food (Nahrung)
# die Nahrung sollte mit Zufallszahlen von 300 und 2000 erstellt werden.

# Aufgabe 5
# erweitere deine Magische Methode __str__() indem du
# dir den Namen deines Planeten, Die Bevölkerungszahl und
# die Nahrung in der Konsole ausgeben lassen kannst.
# Erstelle einen Planeten ung gib ihm als Parameter einen Namen


# Aufgabe 6
# Lösche die Instanz in deiner Klasse Planet und auch den Printbefehl
# erstelle eine weitere Datei, die ein Hauptmenü enthält, bei dem du
# folgende Auswahlmöglichkeiten hast:
# 1: Neuen Planeten erstellen
# 2: Menschen erschaffen
# 3: Programm beenden
# erstelle dein Hauptmenü als Klasse

# Aufgabe 7
# erschaffe einen neuen Planeten wenn der Benutzer die 1 wählt und
# gib aus: Der neue Planet [Planetenname] wurde erstellt
# benutze die time.sleep() Funktion um nach einer bestimmten Zeit
# die Konsole zu löschen und die aktuell in einer Liste
# gespeicherten Planeten über dem Hauptmenü auszugeben.

# Aufgabe 8
# Erweitere deine Klasse Planet um die Rohstoffe:
# Holz, Stein, und Gold.
# Die Werte für Holz und Stein sollten zufällig zwischen
# 1500 und 2000 sein.
# Gold hat den Wert 200
# Um zu testen ob alles funktioniert, gib deine Planeten
# mit allen verfügbaren Rohstoffen über dem Hauptmenü aus.

# Aufgabe 9
# Erstelle eine neue Datei mit der Klasse Human.
# füge auch dieser Klasse eine magische Methode
# __str__() hinzu, die jedes Objekt formatiert ausgeben kann.

# Aufgabe 10
# Erstelle in der Klasse Human einen Konstruktor, der als
# Instanzattribute einen Namen, ein Alter und einen Beruf
# bei dem instanziieren eines neuen Menschen zuweist

# Aufgabe 11
# Erweitere dein Menü, dass nach der Wahl von 2 ein Menü
# erscheint, welches dich fragt, auf welchem Planeten du
# einen Menschen hinzufügen möchtest.
# Danach soll der Benutzer gefragt werden, welchen Namen,
# Alter und Beruf der neue Mensch bekommen soll.

# Aufgabe 12
# füge den neu erstellten Menschen dem gewählten Planeten hinzu,
# indem du eine Methode mit dem Namen add_human in der Klasse
# Planeten hinzufügst übergebe dieser Methode den neu erstellten
# Menschen und schau nach, ob die Bevölkerungszahl sich nach der
# Ausgabe des Planeten verändert hat.

# Aufgabe 13
# Es sollen nur Menschen zu einem Planeten hinzugefügt werden,
# bis die maximale Bevölkerungszahl von 20 erreicht ist.

# TIPP: Benutze öfter os.system('cls') um die Konsole sauber und
# übersichtlich zu halten. Falls du Linux benutzt finde raus wie
# du den Befehl erweitern kannst, damit deine
# Konsole aufgeräumt bleibt. :)


# Teil 2
# ( Ein Hoch auf den Kapitalismus!!! )
# Aufgabe 1
# Erweitere dein Menü um den Punkt Gebäude bauen
# baue ein Menü wo du einen Planeten auswählst, auf dem du ein
# Gebäude bauen möchtest Wenn du einen Planeten ausgewählt hast,
# gib eine Liste mit Dictionaries von Gebäuden aus einer Klasse
# Structures aus, die man bauen kann: Rathaus, Jägerhütte, Bauernhof,
# Steinmetz, Holzfällerhütte und Goldmine implementiere folgende Kosten
# nach folgendem Muster in einer Liste mit Dictionaries:
# "name": "Rathaus", "food_costs": 50, "stone_costs": 1200,"wood_costs": 1200,"gold_costs": 80,
# "name": "Jagdhütte", "food_costs": 10, "stone_costs": 10 ,"wood_costs": 200,"gold_costs": 30,
# "name": "Bauernhof", "food_costs": 20, "stone_costs":  400,"wood_costs": 1200,"gold_costs": 50,
# "name": "Holzfällerhütte", "food_costs": 10, "stone_costs":100  ,"wood_costs": 300,"gold_costs": 25,
# "name": "Steinbruch", "food_costs": 15, "stone_costs":100  ,"wood_costs": 1200,"gold_costs": 25,
# "name": "Goldmine", "food_costs": 40, "stone_costs":1500  ,"wood_costs": 1500,"gold_costs": 30
# TIPP: Du stößt eventuell auf die Möglichkeit eine statische Methode zu definieren.
# Vielleicht hast du Lust deinem Team zu erklären was das ist ?

# Aufgabe 2
# Um ein Gebäude überhaupt bauen zu können, benötigst du ein Rathaus.
# Baue zuerst ein Rathaus auf deinem Planeten, damit du andere Gebäude bauen kannst
# und neue Menschen überhaupt auf dem neuen Planeten hinzufügen kannst.
# implementiere eine Methode die berechnet, ob du überhaupt genug Resourcen
# auf deinem Planeten hast, um überhaupt ein Rathaus bauen zu können
# Erweitere deine Klassenattribute so, das bei dem Instanzieren eines
# Planeten noch kein Rathaus gebaut wurde. Wenn du einen Menschen auf dem
# Planeten hinzufügen möchtest
# prüfe zuerst ob ein Rathaus vorhanden ist. Wenn nicht, baue erst ein Rathaus.

# Aufgabe 3 ( Räum dein Zimmer auf! Refactoring )
# Bestimmt ist dir aufgefallen, das die Planetenauswahl redundant ist.
# Sie steht einmal in deiner Methode in der du einen Menschen erschaffen
# willst und wahrscheinlich
# findest du weiteren Code, den du in einer einzigen Funktion auslagern könntest.
# Mit anderen Worten: Baue eine Methode, die nur dafür zuständig ist, einen
# Planeten auszuwählen und den ausgewählten Planeten zurück zu geben.

""" def set_cursor_position(self, row, col):
        sys.stdout.write(f"\033[{row};{col}H")
        sys.stdout.flush() """
# Aufgabe 4
# Menschen wären nicht Menschen, wenn sie nicht Resourcen verbrauchen würden.
# Für jeden Menschen den du neu auf einem Planeten erstellst, benötigst du einmalig 100 Nahrung.
# Jeder Mensch der auf einem Planeten platziert wird, verbraucht pro Sekunde 3 Nahrung
# Baue deine Konsole so um, Das die Planeten mit den jeweils aktuellen Resourcen
# jede Sekunde aktualisiert angezeigt werden.
# So gehst du am besten vor:
# 1. importiere das Modul sys
# 2. verwende wenn du möchtest diesen Code um den Cursor in deiner Konsole bei
# Bedarf an eine bestimmte Stelle zu setzen, verwende sie als Hilfsfunktion:
# 3. Um die Kontrolle über deine Konsole zu behalten, das deine Ausgaben wie
# gewünscht an bestimmten Stellen verändert werden, kannst du diese Hilfsfunktion verwenden:
""" def update_line(self,line, text):
        sys.stdout.write(f"\033[{line};0H{text}\033[K")
        sys.stdout.flush() """
# 4. Beachte das print Ausgaben sich immer an das Ende einer Zeile nach einem
# Befehl setzen. Sei vorsichtig beim setzen von printbefehlen.
# Tipp: verwende bei Schleifen den Printbefehl, da du sonst bei jeden
# Schleifendurchlauf die aktuelle Zeite mit dem Inhalt einer Liste übschreibst.
# Tipp: Um beispielsweise den Cursor im Terminal auf eine gewünschte Zeile zu setzen verwende:
#       self.set_cursor_position(1, 0) oder wenn du etwas berechnen musst:
#       self.set_cursor_position(len(planets) + 2, 0)
# Tipp: Um eine Zeile zu aktualisieren, wie beispielsweise die dynamische Planeteninfromation:
#       self.update_line(1, "Es sind nocj keine Planeten vorhanden!")
#       oder wenn du immer eine bestimmte Stelle dynamisch berechnen möchtest:
#       self.update_line(len(planets) + len(available_structures) + 3, "Bitte wähle ein Gebäude aus:")