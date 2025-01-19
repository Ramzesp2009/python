print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = int(input())

if gehalt > 2500:
    print("Es ergibt sich eine Steuer von", (gehalt / 100) * 22, "Euro")
else:
    print("Es ergibt sich eine Steuer von", (gehalt / 100) * 18, "Euro")