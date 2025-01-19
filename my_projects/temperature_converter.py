import tkinter

def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} C"

window = tkinter.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

frm_entry = tkinter.Frame(master=window)
ent_temperature = tkinter.Entry(master=frm_entry, width=10)
lbl_temp = tkinter.Label(master=frm_entry, text="F")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tkinter.Button(
    master=window,
    text="-",
    command=fahrenheit_to_celsius
)
lbl_result = tkinter.Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()