import tkinter

def aktion(self):
    lbWert['text'] = f"Aktion: {scWert.get()} km/h"


def ausgabe():
    lbWert['text'] = f"Ausgabe: {scWert.get()} km/h"


def ende():
    fenster.destroy()


fenster = tkinter.Tk()
fenster.title('Scale')
fenster.resizable(0,0)

wert = tkinter.IntVar()
wert.set(100)

scWert = tkinter.Scale(fenster, length=300, orient='horizontal', from_=0, to=200,
                       resolution=5, tickinterval=20, label='km/h')
scWert.grid(row=0, column=0, padx=10, pady=10)

buAusgabe = tkinter.Button(fenster, text='Ausgabe', command=ausgabe, width=10)
buAusgabe.grid(row=1, column=0, padx=10, pady=10, sticky='w')

lbWert = tkinter.Label(fenster, text='Start: 100 km/h')
lbWert.grid(row=2, column=0, padx=10, pady=10, sticky='w')

buEnde = tkinter.Button(fenster, text='Ende', command=ende, width=10)
buEnde.grid(row=3, column=1, padx=10, pady=10)

fenster.mainloop()
