import horses


def kunden_begrussung():
    begruessung = "Willkommen in Pferdchenshop"
    print(begruessung)
    print("Welches Pferdchen möchtest du kaufen?")
    print(f"""
        Wählen Sie 1 für Kleinpferd {horses.klein_pferd :.2f} $,
        wählen Sie 2 für Mittlpferd {horses.mittl_pferd :.2f} $
        und wählen Sie 3 für Grosspferd {horses.gross_pferd:.2f} $
    """)
