# kontrol function
import horses


def eingabe_kontrolle(x):
    if x == 1:
        # gesamt_kosten = versand_kosten + klein_pferd
        print(f"Sie haben sich für das kleine Pferd für {horses.klein_pferd:.2f} $ entschieden.")
    elif x == 2:
        print(f"Sie haben sich für das mittlere Pferd für {horses.mittl_pferd :.2f} $ entschieden.")
    elif x == 3:
        print(f"Sie haben sich für das große Pferd für {horses.gross_pferd :.2f} $ entschieden.")
    else:
        print("Ungültige Auswahl, bitte wählen Sie 1, 2 oder 3.")
