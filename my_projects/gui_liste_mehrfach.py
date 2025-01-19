import tkinter

def ausgabe():
    ausgabe = ""
    for index in liAuswahl.curselection():
        ausgabe += f"{liAuswahl.get(index)}\n"
    lbAusgabe["text"] = ausgabe


def ende():
    fenster.destroy()


fenster = tkinter.Tk()
fenster.title("Einfach")
fenster.resizable(0,0)
lbAuswahl = tkinter.Label(fenster, text="Ihre Auswahl:")
lbAuswahl.grid(row=0, column=0, sticky="w", padx=15, pady=15)

frAuswahl = tkinter.Frame(fenster)
frAuswahl.grid(row=0, column=0, padx=15, pady=15)

sbAuswahl = tkinter.Scrollbar(frAuswahl, orient="vertical")
liAuswahl = tkinter.Listbox(frAuswahl, height=4, yscrollcommand=sbAuswahl.set, selectmode="multiple")
sbAuswahl["command"] = liAuswahl.yview

stadt = [
         'Hamburg',
         'Stuttgart',
         'Berlin',
         'Dortmund',
         'Trier',
         'Duisburg',
         'Potsdam',
         'Halle',
         'Flensburg',
         'Augsburg',
         ]
for s in stadt:
    liAuswahl.insert("end", s)
liAuswahl.grid(row=0, column=0)
sbAuswahl.grid(row=0, column=0, sticky="sn")

buAusgabe = tkinter.Button(fenster, text="Ausgabe", command=ausgabe, width=10)
buAusgabe.grid(row=2, column=0, sticky="w", padx=15, pady=15)

lbAusgabe = tkinter.Label(fenster, text="(leer)", height=10, anchor="n")
lbAusgabe.grid(row=3, column=0, sticky="w", padx=15, pady=15)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width=10)
buEnde.grid(row=4, column=2, padx=15, pady=15)

fenster.mainloop()
