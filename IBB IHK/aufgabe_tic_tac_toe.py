# Aufgabe 1
# erstelle mit einer List Comprehension 3 Listen mit einem Leerzeichen in
# einer Liste mit dem Namen Spielfeld
# gib deine List Comprehension aus
# die Ausgabe sollte so aussehen: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# a = [[' ' for i in range(3)] for i in range(3)]
# print(a)


# Aufgabe 2
# 2.1 Suche im Internet nach der Methode .join() und erkläre im Detail was diese macht
# 2.2 Schreibe eine Funktion mit dem Namen zeichne Spielfeld mit einer for Schleife,
# die jede Liste deiner List Comprehension untereinander ausgibt
# 2.3 Benutze die join Methode, um die Listen mit einem " | " Zeichen miteinander zu
# verbinden und gebe sie in der Console aus.
# 2.4 füge jeder Liste in einer Reihe einen Boden mit "-" hinzu und gebe dein Spielfeld
# in der Console aus. (Tipp: 9 Trennstriche sehen gut und symmetrisch aus)
# Dein Ergebnis sollte etwa wie folgt aussehen:
#
#  |   |
# ---------
#  |   |
# ---------
#  |   |
# ---------



def zeichne_spielfeld(lists: list):
    for list in lists:
        print((' | ').join(list))
        print('_________')



# Aufgabe 3
# 3.1 Baue eine Hauptfunktion mit dem Namen starte_spiel(), kopiere deine List Comprehension mit deinem
#     Spielfeld in die Funktion, so das dein Spielfeld bei dem Aufruf der Funktion erstellt wird
# 3.2 Definiere eine Variable mit dem Namen aktueller_spieler = 'X' in deiner Funkion
# 3.3 Baue eine While Schleife, in deiner starte_spiel() Funktion, die bei dem Start der Schleife
#     deine Funktion zeichne_spielfeld aufruft. (TIPP: Vergiss nicht die Parameterübergabe)
# 3.4 Fordere innerhalb deiner While Schleife eine Eingabe an, welche die Zeile mit einer Zahl empfängt
#     und speichere den Wert der Eingabe in der Variable zeile. Dieser Wert wird später auf den Index deines
#     Feldes zugreifen
# 3.5 Fordere innerhalb deiner While Schleife eine weitere Eingabe an, welche die Spalte mit einem Zahlenwert
#     empfängt, die später dem Index der Spalte zugewiesen wird und speichere den Wert der
#     Eingabe in einer Variablen mit dem Namen spalte
#     (TIPP: Aus der Kombination deiner Eingabe ergeben sich später die Indizes und somit die Stelle an der
#     deine Wahl platziert wird)




def starte_spiel():
    lists = [[' ' for i in range(3)] for i in range(3)]
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(lists)
        zeile = int(input("Enter one figure please:    "))
        spalter = int(input("Enter one figure please:    "))
        lists[zeile][spalter] = aktueller_spieler

# Aufgabe 4
# Du hast ein 2 Dimensionales Spielfeld gebaut, auf dessen Felder du
# zugreifen kannst. Finde heraus, wie du das Zeichen deines aktuellen Spielers
# auf die Felder der getätigten Eingabe setzen kannst und erweitere deine
# Funktion starte_spiel() mit der Zuweisung X auf die Eingabe des Spielers


starte_spiel()
# Aufgabe 5
# Wechsle den aktuellen Spieler in deiner While Schleife von "X" auf "O"
# und falls dieser Spieler schon auf "O" stehen sollte, wechsle ihn wieder zu "X"
# Teste mal aus, ob es schon funktioniert


# Aufgabe 6
# Atme mal tief durch, trink nen Schluck und wenn du fertig bist, zeige
# mit einem print Befehl an, welcher Spieler grade bei dem neuen Schleifendurchlauf an
# der Reihe ist.


# Aufgbe 7
# Begründe warum du die Zahlen 0 - 2 eingeben musst.


# Aufgabe 8
# Was wäre eine Lösung, wenn du die Zahlen 1 - 3 eingeben möchtest,
# weil sich diese Eingabe intuitiver anfühlt?
# Welche Problematik tritt auf und wie können wir diese beheben und umsetzen ?


# Aufgabe 9
# Wenn du es bis hierhin schon geschafft hast, herzlichen Glückwunsch.
# Jetzt folgen noch mehr Aufgaben. Vielleicht machst du ein kurzes Brainstorming darüber,
# welche Aufgaben das sein könnten.