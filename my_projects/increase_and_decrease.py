import tkinter

def decrease():
    velue = int(lbl_value["text"])
    lbl_value["text"] = f"{velue - 1}"


def increase():
    velue = int(lbl_value["text"])
    lbl_value["text"] = f"{velue + 1}"


window = tkinter.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tkinter.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tkinter.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tkinter.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()