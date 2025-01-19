def halbieren(wert):
    print(wert)
    wert = wert / 2
    if wert > 0.0005:
        halbieren(wert)

# Programm
halbieren(3)