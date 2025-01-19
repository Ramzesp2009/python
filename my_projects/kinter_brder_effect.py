import tkinter

border_effects = {
    "flat": tkinter.FLAT,
    "sunken": tkinter.SUNKEN,
    "raised": tkinter.RAISED,
    "groove": tkinter.GROOVE,
    "ridge": tkinter.RIDGE,
}

window = tkinter.Tk()

for relief_name, relief in border_effects.items():
    # 1
    frame = tkinter.Frame(master=window, relief=relief, borderwidth=5)
    # 2
    frame.pack(side=tkinter.LEFT)
    # 3
    label = tkinter.Label(master=frame,text=relief_name)
    label.pack()

window.mainloop()