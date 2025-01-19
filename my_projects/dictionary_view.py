dc = {"Peter": 31, "Julia": 28, "Werner": 35}
print("Dictionary: ", dc)

k = dc.keys()
print("Schlussel:", k)
for schluessel in k:
    print(schluessel)
if "Werner" in k:
    print("Schlussel Werner ist enthalten")
print()

v = dc.values()
print("Werte:", v)
for wert in v:
    print(wert)
if 31 in v:
    print("Wert 31 ist enthalten")
print()

i = dc.items()
print("Items:", i)
for k, v in i:
    print(f"Schlussel {k}, Wert {v}")