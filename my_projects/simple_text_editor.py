import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """to open the file for correction"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tkinter.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tkinter.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """ to save currently file how new"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tkinter.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


window = tkinter.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(2, minsize=800, weight=1)

txt_edit = tkinter.Text(window)
fr_buttons = tkinter.Frame(window, relief=tkinter.RAISED, bd=2)
btn_open = tkinter.Button(fr_buttons, text="Open", command=open_file)
btn_save = tkinter.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
