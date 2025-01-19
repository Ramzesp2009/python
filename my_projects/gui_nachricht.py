import tkinter, tkinter.messagebox as mb


def info():
    mb.showinfo("Box", "Info")


def warning():
    mb.showwarning("Box", "Warnung")


def error():
    mb.showerror("Box", "Error")


def yesno():
    antwort = mb.askyesno("Box", "Yes or no")
    lbAusgabe["Text"] = "Yes" if antwort == 1 else "No"


def frage():
    msg_box = mb.Message(fenster, type=mb.ABORTRETRYIGNORE, icon=mb.QUESTION,
                         title="Box", message="Abbrechen, Wiederholen oder Ignorieren")
    antwort = msg_box.show()
    if antwort == "abort":
        lbAusgabe["text"] = "Abbrechen"
    elif antwort == "retry":
        lbAusgabe["text"] = "Wiederholen"
    else:
        lbAusgabe["text"] = "Ignorieren"


def ende():
    fenster.destroy()


fenster = tkinter.Tk()

buInfo = tkinter.Button(fenster, text="Info", width=20, command=info)
buInfo.grid(row=0, column=0, padx=10, pady=10)

buWarning = tkinter.Button(fenster, text="Warning", width=20, command=warning)
buWarning.grid(row=0, column=1, padx=10, pady=10)

buError = tkinter.Button(fenster, text="Error", width=20, command=error)
buError.grid(row=0, column=2, padx=10, pady=10)

buYesNo = tkinter.Button(fenster, text="Yes/No", width=20, command=yesno)
buYesNo.grid(row=1, column=0, padx=10, pady=10)

buFrage = tkinter.Button(fenster, text="Allgemeine Frage",
                         width=20, command=frage)
buFrage.grid(row=1, column=1, padx=10, pady=10)

lbAusgabe = tkinter.Label(fenster, text="(leer)")
lbAusgabe.grid(row=1, column=2, padx=10, pady=10)

buEnde = tkinter.Button(fenster, text="Ende", width=20, command=ende)
buEnde.grid(row=2, column=2, padx=10, pady=10)

fenster.mainloop()
