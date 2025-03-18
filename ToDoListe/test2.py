import customtkinter
import sqlite3
from datetime import datetime


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


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, task_manager, **kwargs):
        super().__init__(master, **kwargs)
        self.task_manager = task_manager

        self.add("Створити завдання")
        self.add("Переглянути завдання")

        self.create_task_tab()
        self.view_tasks_tab()
        self.load_tasks()

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
        self.todo_listbox = customtkinter.CTkTextbox(task_tab, width=300, height=200)
        self.todo_listbox.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.move_button = customtkinter.CTkButton(task_tab, text="➡", command=self.complete_task)
        self.move_button.grid(row=1, column=1, padx=10, pady=5)

        self.done_listbox = customtkinter.CTkTextbox(task_tab, width=300, height=200)
        self.done_listbox.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

        self.delete_button = customtkinter.CTkButton(task_tab, text="Видалити завдання", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10, sticky="se")

    def load_tasks(self):
        self.todo_listbox.delete("1.0", "end")
        self.done_listbox.delete("1.0", "end")

        for task in self.task_manager.get_tasks(completed=False):
            self.todo_listbox.insert("end", f"{task[1]} (до {task[2]})\n")

        for task in self.task_manager.get_tasks(completed=True):
            self.done_listbox.insert("end", f"{task[1]} (до {task[2]})\n")

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
        self.task_manager.complete_task(1)  # Потрібно отримати ID вибраного завдання
        self.load_tasks()

    def delete_task(self):
        self.task_manager.delete_task(1)  # Потрібно отримати ID вибраного завдання
        self.load_tasks()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x450")
        self.title("Менеджер завдань")

        self.task_manager = TaskManager()
        self.tab_view = MyTabView(master=self, task_manager=self.task_manager)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()

