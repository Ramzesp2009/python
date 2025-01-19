import tkinter
window = tkinter.Tk()
frame_a = tkinter.Frame()
frame_b = tkinter.Frame()
label_a = tkinter.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
label_b = tkinter.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()
# frame_b.pack()

window.mainloop()