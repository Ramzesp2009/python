zahl = 1
while zahl != 0:
    print("Geben Sie bitte Inch ein.")
    zahl = int(input().strip())
    if zahl == 0:
        break
    zentimetr = zahl * 2.54
    print(f"Eingegebene Zahl in Inch {zahl} ist {zentimetr} in cm")
    print("So lange die Eingabe ungleich 0 ist")
print("Auf wiedersehen")