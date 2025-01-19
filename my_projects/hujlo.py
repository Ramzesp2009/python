import tkinter

def kill_putin():
    message["text"] = "Putin died"

window = tkinter.Tk()
window.title("Хуйло")
buton = tkinter.Button(window, text="Kill Putin", command=kill_putin, font=22)
buton.grid()
message = tkinter.Label(window, text="Putin live", font=22)
message.grid()

# buton.pack()
window.mainloop()