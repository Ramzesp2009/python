from tkinter import *

class ToDoList:
    def __init__(self, root):
        # self.task = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task, activeforeground="blue")
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task, activeforeground="red")
        self.placeholder = "напиши тут завдання"

        # GUI Layout
        self.entry.insert(0, self.placeholder)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        self.entry.pack(pady=10, padx=10, fill="x")
        self.addButton.pack(pady=10, padx=10, fill="x")
        self.listbox.pack(pady=10, padx=10, fill="x")
        self.delButton.pack(pady=10, padx=10, fill="x")

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass
    
    def clear_placeholder(self, event):
        """При фокусуванні очищує поле, якщо воно містить текст-заповнювач"""
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, END)
            self.entry.config(fg="black")  # Змінюємо колір тексту на чорний

    def add_placeholder(self, event):
        """При втраті фокусу повертає текст-заповнювач, якщо поле порожнє"""
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg="gray")  # Змінюємо колір тексту на сірий


root = Tk()
root.title("Python To-Do List")
root.geometry("300x400") # Set the window size
to_do_list = ToDoList(root)
root.mainloop()
