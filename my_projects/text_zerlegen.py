text = "Das ist ein Satz"
print("Text:", text)
liste = text.split()
for i in range(0, len(liste)):
    print("Element:", i, liste[i])
print()

text = "Maier;Hans;6713;3.500,00;15.03.62"
print("Text:", text)
liste = text.split(";")
for i in range(0, len(liste)):
    print("Element:", i, liste[i])
