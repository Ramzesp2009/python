print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = int(input())

if gehalt > 4000:
    print("Es ergibt sich eine Steuer 26% von", (gehalt / 100) * 26, "Euro")
elif gehalt > 2500:
    print("Es ergibt sich eine Steuer 22% von", (gehalt / 100) * 22, "Euro")
else:
    print("Es ergibt sich eine Steuer 18% von", (gehalt / 100) * 18, "Euro")