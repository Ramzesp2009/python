import customtkinter
import sqlite3
from datetime import datetime
import tkinter as tk  # Додаємо стандартний Tkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, task_manager, **kwargs):
        super().__init__(master, **kwargs)
        self.task_manager = task_manager

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.tabs = ["Створити завдання", "Переглянути завдання"]
        for tab_name in self.tabs:
            self.add(tab_name)

        self.create_task_tab()
        self.view_tasks_tab()
        self.load_tasks()

        for tab_name in self.tabs:
            self.tab(tab_name).grid_columnconfigure(0, weight=1)
            self.tab(tab_name).grid_rowconfigure(3, weight=1)

    def create_task_tab(self):
        task_tab = self.tab("Створити завдання")
        self.label_name = customtkinter.CTkLabel(task_tab, text="Назва завдання:")
        self.label_name.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.entry_name = customtkinter.CTkEntry(task_tab, width=300)
        self.entry_name.grid(row=0, column=1, padx=20, pady=10)

        self.label_date = customtkinter.CTkLabel(task_tab, text="Дата виконання:")
        self.label_date.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.entry_date = customtkinter.CTkEntry(task_tab, width=300)
        self.entry_date.grid(row=1, column=1, padx=20, pady=10)
        self.entry_date.insert(0, datetime.today().strftime("%Y-%m-%d"))

        self.button_save = customtkinter.CTkButton(task_tab, text="Зберегти", command=self.save_task)
        self.button_save.grid(row=2, column=1, padx=20, pady=20, sticky="se")

    def view_tasks_tab(self):
        task_tab = self.tab("Переглянути завдання")

        task_tab.grid_columnconfigure(0, weight=1)  
        task_tab.grid_columnconfigure(2, weight=1)  
        task_tab.grid_rowconfigure(1, weight=1)  

        # Заголовок для списку невиконаних завдань
        self.label_todo = customtkinter.CTkLabel(task_tab, text="Невиконані завдання:", font=("Arial", 14, "bold"))
        self.label_todo.grid(row=0, column=0, padx=20, pady=10)

        # Ліва колонка (невиконані завдання)
        self.todo_listbox = tk.Listbox(task_tab, width=40, height=10)
        self.todo_listbox.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.todo_scrollbar = tk.Scrollbar(task_tab, orient="vertical", command=self.todo_listbox.yview)
        self.todo_scrollbar.grid(row=1, column=0, sticky="nse")
        self.todo_listbox.config(yscrollcommand=self.todo_scrollbar.set)

        # Створюємо фрейм для кнопок переміщення
        self.buttons_frame = customtkinter.CTkFrame(task_tab)
        self.buttons_frame.grid(row=1, column=1, padx=10, pady=5)

        # Кнопка переміщення завдання у "виконані"
        self.move_button = customtkinter.CTkButton(self.buttons_frame, text=">>>", width=40, command=self.complete_task)
        self.move_button.grid(row=0, column=1, padx=5, pady=5)

        # Кнопка переміщення завдання у "невиконані"
        self.undo_button = customtkinter.CTkButton(self.buttons_frame, text="<<<", width=40, command=self.undo_task)
        self.undo_button.grid(row=1, column=1, padx=5, pady=5)

        # Заголовок для списку виконаних завдань
        self.label_done = customtkinter.CTkLabel(task_tab, text="Виконані завдання:", font=("Arial", 14, "bold"))
        self.label_done.grid(row=0, column=2, padx=10, pady=10)

        # Права колонка (виконані завдання)
        self.done_listbox = tk.Listbox(task_tab, width=40, height=10)
        self.done_listbox.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

        self.done_scrollbar = tk.Scrollbar(task_tab, orient="vertical", command=self.done_listbox.yview)
        self.done_scrollbar.grid(row=1, column=2, sticky="nse")
        self.done_listbox.config(yscrollcommand=self.done_scrollbar.set)

        # Кнопка видалення
        self.delete_button = customtkinter.CTkButton(task_tab, text="Видалити завдання", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10, sticky="se")

    def load_tasks(self):
        self.todo_listbox.delete(0, "end")
        self.done_listbox.delete(0, "end")

        self.todo_tasks = {}  
        self.done_tasks = {}

        for task in self.task_manager.get_tasks(completed=False):
            task_str = f"{task[1]} (до {task[2]})"
            self.todo_listbox.insert("end", task_str)
            self.todo_tasks[self.todo_listbox.size() - 1] = task[0]  

        for task in self.task_manager.get_tasks(completed=True):
            task_str = f"{task[1]} (до {task[2]})"
            self.done_listbox.insert("end", task_str)
            self.done_tasks[self.done_listbox.size() - 1] = task[0]  

    def save_task(self):
        name = self.entry_name.get()
        due_date = self.entry_date.get()
        if name:
            self.task_manager.add_task(name, due_date)
            self.load_tasks()
            self.entry_name.delete(0, "end")
            self.entry_date.delete(0, "end")
            self.entry_date.insert(0, datetime.today().strftime("%Y-%m-%d"))

    def complete_task(self):
        selected_index = self.todo_listbox.curselection()
        if selected_index:
            task_id = self.todo_tasks[selected_index[0]]
            self.task_manager.complete_task(task_id)
            self.load_tasks()

    def undo_task(self):
        selected_index = self.done_listbox.curselection()
        if selected_index:
            task_id = self.done_tasks[selected_index[0]]
            self.task_manager.undo_task(task_id)
            self.load_tasks()

    def delete_task(self):
        selected_index = self.todo_listbox.curselection() or self.done_listbox.curselection()
        if selected_index:
            task_id = self.todo_tasks.get(selected_index[0]) or self.done_tasks.get(selected_index[0])
            if task_id:
                self.task_manager.delete_task(task_id)
                self.load_tasks()


class TaskManager:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )""")
        self.conn.commit()

    def add_task(self, name, due_date):
        self.cursor.execute("INSERT INTO tasks (name, due_date) VALUES (?, ?)", (name, due_date))
        self.conn.commit()

    def get_tasks(self, completed=False):
        self.cursor.execute("SELECT id, name, due_date FROM tasks WHERE completed = ?", (int(completed),))
        return self.cursor.fetchall()

    def complete_task(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.geometry("700x450")
        self.title("Менеджер завдань")

        self.task_manager = TaskManager()
        self.tab_view = MyTabView(master=self, task_manager=self.task_manager)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
