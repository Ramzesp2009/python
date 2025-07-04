import customtkinter
from datetime import datetime

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Список вкладок
        self.tabs = ["Створити завдання", "Переглянути завдання"]

        # Створення вкладок
        for tab_name in self.tabs:
            self.add(tab_name)

        # Додавання полів у вкладку "Створити завдання"
        self.create_task_tab()

        # Додавання списку завдань у вкладку "Переглянути завдання"
        self.view_tasks_tab()

        # Налаштовуємо розширення вкладок
        for tab_name in self.tabs:
            self.tab(tab_name).grid_columnconfigure(0, weight=1)
            self.tab(tab_name).grid_rowconfigure(3, weight=1)

        # Список завдань
        self.tasks = []

    def create_task_tab(self):
        """ Додає поля для створення завдання у вкладку 'Створити завдання' """
        task_tab = self.tab("Створити завдання")

        # Поле для введення назви завдання
        self.label_name = customtkinter.CTkLabel(task_tab, text="Назва завдання:")
        self.label_name.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.entry_name = customtkinter.CTkEntry(task_tab, width=300)
        self.entry_name.grid(row=0, column=1, padx=20, pady=10)

        # Поле для вибору дати виконання
        self.label_date = customtkinter.CTkLabel(task_tab, text="Дата виконання:")
        self.label_date.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.entry_date = customtkinter.CTkEntry(task_tab, width=300)
        self.entry_date.grid(row=1, column=1, padx=20, pady=10)

        # Автоматично встановлюємо поточну дату
        today = datetime.today().strftime("%Y-%m-%d")
        self.entry_date.insert(0, today)

        # Розширюємо простір перед кнопкою
        task_tab.grid_rowconfigure(2, weight=1)

        # Кнопка для створення завдання (зберегти)
        self.button_save = customtkinter.CTkButton(task_tab, text="Зберегти", command=self.save_task)
        self.button_save.grid(row=3, column=1, padx=20, pady=20, sticky="se")

    def view_tasks_tab(self):
        """ Додає список завдань у вкладку 'Переглянути завдання' """
        task_tab = self.tab("Переглянути завдання")

        # Список невиконаних завдань
        self.label_todo = customtkinter.CTkLabel(task_tab, text="Завдання для виконання")
        self.label_todo.grid(row=0, column=0, padx=10, pady=5)

        self.todo_listbox = customtkinter.CTkTextbox(task_tab, width=250, height=200)
        self.todo_listbox.grid(row=1, column=0, padx=10, pady=5)

        # Кнопка для перенесення завдання
        self.move_button = customtkinter.CTkButton(task_tab, text="➡", width=50, command=self.move_task)
        self.move_button.grid(row=1, column=1, padx=10, pady=5)

        # Список виконаних завдань
        self.label_done = customtkinter.CTkLabel(task_tab, text="Виконані завдання")
        self.label_done.grid(row=0, column=2, padx=10, pady=5)

        self.done_listbox = customtkinter.CTkTextbox(task_tab, width=250, height=200)
        self.done_listbox.grid(row=1, column=2, padx=10, pady=5)

    def save_task(self):
        """ Зберігає завдання у список і додає його у вкладку 'Переглянути завдання' """
        task_name = self.entry_name.get()
        due_date = self.entry_date.get()

        if task_name:
            task = f"{task_name} (до {due_date})"
            self.tasks.append(task)
            self.todo_listbox.insert("end", task + "\n")  # Додаємо у список невиконаних завдань
            print(f"Збережено завдання: {task_name}, дата виконання: {due_date}")
        else:
            print("Помилка: введіть назву завдання!")

    def move_task(self):
        """ Переміщує вибране завдання в список виконаних """
        selected_task = self.todo_listbox.get("1.0", "2.0").strip()  # Отримуємо перший рядок

        if selected_task:
            self.done_listbox.insert("end", selected_task + "\n")  # Додаємо в список виконаних
            self.todo_listbox.delete("1.0", "2.0")  # Видаляємо перший рядок зі списку невиконаних
            print(f"Завдання виконано: {selected_task}")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Менеджер завдань")

        # Дозволяємо вкладкам розтягуватися разом із вікном
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
