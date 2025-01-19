import tkinter

window = tkinter.Tk()

frame1 = tkinter.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

frame2 = tkinter.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

frame3 = tkinter.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

window.mainloop()