# 1 Erstelle 5 Listen, wobei jeweils eine Liste nur strings, eine andere nur integer,
# eine weitere nur floats beinhaltet. Was in den anderen beiden steht ist egal
print("Aufgabe 1")
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
float_list = [i * 1.0 for i in range(1, 11)]
str_list = ['one','two','three','four','five',
            'six','seven','eight','nine','ten']
dictionary_list = {x: x * 5 for x in range(1, 11)}
tuple_list = tuple([i for i in range(1, 11)])
print("int_list", int_list)
print("float_list", float_list)
print("str_list", str_list)
print("dictionary_list", dictionary_list)
print("tuple_list", tuple_list)
print()

# 2 Hänge 3 Werte an deine 1. Liste an
print("Aufgabe 2")
werte = [11, 12, 13]
int_list.extend(werte)
print(int_list)
print()

# 3 Nimm deine 2. Liste und hänge sie an deine erste Liste,
# lass sie dir danach ausgeben
print("Aufgabe 3")
new_int_list = [14, 15, 16, 17, 18, 19, 20]
int_list.extend(new_int_list)
print(int_list)
print()

# 4 Füge deinen Namen und 2 weitere Namen deiner Klassenkameraden
# deiner 1 Liste an Position 3, 4 und 6 hinzu
print("Aufgabe 4")
str_list.insert(3, 'Pavlo')
str_list.insert(4, 'Mike')
str_list.insert(6, 'Evander')
print(str_list)
print()

# 5 Entferne einen Wert mit der Methode remove aus deiner 4. Liste.
# begründe warum der Wert trotzdem noch in der Liste vorhanden sein könnte
print("Aufgabe 5")
print(int_list)
int_list.remove(1)
print(int_list)
print()

# 6 Werfe das letzte Element aus deiner 1. Liste raus.
print("Aufgabe 6")
print(int_list.pop())
# int_list.remove(int_list[-1])
print(int_list)
print()

# 7 Lösche den Inhalt aus deiner 5. Liste und gib sie aus,
# um zu prüfen ob die Liste wirklich leer ist
print("Aufgabe 7")
# print(float_list)
# float_list.clear()
# print(float_list)
print()

# 8 Sortiere deine 2 Liste absteigend und gib sie aus
print("Aufgabe 8")
print(float_list)
float_list.reverse()
print(float_list)
print()

# 9-10 Kopiere deine 4. Liste und lasse sie dir ausgeben mit dem
# Satz: "Das ist die Kopie von Liste Füge einen Eintrag in deiner Kopie hinzu,
# lasse dir danach die Kopie und die original Liste ausgeben und schau ob das
# ändern der Kopie die echte Liste verändert hat.
print("Aufgabe 9-10")
new_str_list = str_list.copy()
new_str_list.append("Das ist die Kopie van Liste 4")
print(str_list)
print(new_str_list)
print()

# 11 Zähle wie oft der Name Alex in deiner 1. Liste vorhanden ist
print("Aufgabe 11")
print(str_list.count("Alex"))
print()

# 12 Zähle wie oft dein Name in der 1. Liste vorhanden ist
print("Aufgabe 12")
print(str_list.count("Pavlo"))
print()

# 13 Prüfe wie oft die Zahl 3 in deiner 2. Liste ist
print("Aufgabe 13")
print(int_list.count(3))
print()

# 14 Sortiere die 3 Liste aufsteigend
print("Aufgabe 14")
float_list.sort()
print(float_list)