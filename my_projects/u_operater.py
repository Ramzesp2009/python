print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = int(input())

print("Geben Sie bitte Ihre Familiestand ein: verheiratet (1) oder ledig (2)")
familienstand = int(input())

if gehalt > 4000 and familienstand == 2:
    print("Es ergibt sich eine Steuer 26% von", (gehalt / 100) * 26, "Euro")
elif gehalt > 4000 and familienstand == 1:
    print("Es ergibt sich eine Steuer 22% von", (gehalt / 100) * 22, "Euro")
elif gehalt <= 4000 and familienstand == 1:
    print("Es ergibt sich eine Steuer 22% von", (gehalt / 100) * 22, "Euro")
elif gehalt <= 4000 and familienstand == 2:
    print("Es ergibt sich eine Steuer 18% von", (gehalt / 100) * 18, "Euro")
else:
    print("Sie eingeben falsche Familienstand, probieren Sie bitte noch Mal")