while True:
    print('Geben Sie bitte eine Zahl in Inch ein')
    zahl = input()
    try:
        inch = int(zahl)
        print(f'{inch} in zentimetr wird {inch * 2.54}')
        break
    except:
        print('Fehler bei Umwandlung der Eingabe')