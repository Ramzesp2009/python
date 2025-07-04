import customtkinter
from datetime import datetime

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tabs = ["Створити завдання", "Переглянути завдання"]
        for tab_name in self.tabs:
            self.add(tab_name)

        self.create_task_tab()
        self.view_tasks_tab()

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

        today = datetime.today().strftime("%Y-%m-%d")
        self.entry_date.insert(0, today)

        self.button_save = customtkinter.CTkButton(task_tab, text="Зберегти", command=self.save_task)
        self.button_save.grid(row=2, column=1, padx=20, pady=20, sticky="se")

    def view_tasks_tab(self):
        task_tab = self.tab("Переглянути завдання")

        self.label_todo = customtkinter.CTkLabel(task_tab, text="Завдання для виконання")
        self.label_todo.grid(row=0, column=0, padx=10, pady=5)

        self.todo_listbox = customtkinter.CTkTextbox(task_tab, width=250, height=200, wrap="none")
        self.todo_listbox.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.todo_listbox.bind("<Button-1>", self.select_task)

        self.move_button = customtkinter.CTkButton(task_tab, text="➡", width=50, command=self.move_task)
        self.move_button.grid(row=1, column=1, padx=10, pady=5)

        self.label_done = customtkinter.CTkLabel(task_tab, text="Виконані завдання")
        self.label_done.grid(row=0, column=2, padx=10, pady=5)

        self.done_listbox = customtkinter.CTkTextbox(task_tab, width=250, height=200, wrap="none")
        self.done_listbox.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

        self.delete_button = customtkinter.CTkButton(task_tab, text="Видалити завдання", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10, sticky="se")

        task_tab.grid_columnconfigure(0, weight=1)
        task_tab.grid_columnconfigure(2, weight=1)
        task_tab.grid_rowconfigure(1, weight=1)

        self.selected_task = None
        self.selected_listbox = None

    def save_task(self):
        task_name = self.entry_name.get()
        due_date = self.entry_date.get()

        if task_name:
            task = f"{task_name} (до {due_date})"
            self.todo_listbox.insert("end", task + "\n" + "-" * 60 + "\n")
            self.entry_name.delete(0, "end")
            self.entry_date.delete(0, "end")
            today = datetime.today().strftime("%Y-%m-%d")
            self.entry_date.insert(0, today)
        else:
            print("Помилка: введіть назву завдання!")

    def select_task(self, event):
        self.todo_listbox.tag_remove("selected", "1.0", "end")
        self.done_listbox.tag_remove("selected", "1.0", "end")

        widget = event.widget
        index = widget.index("@%d,%d" % (event.x, event.y))
        line_start = index.split(".")[0] + ".0"
        line_end = index.split(".")[0] + ".end"

        widget.tag_add("selected", line_start, line_end)
        widget.tag_config("selected", background="yellow")

        self.selected_task = widget.get(line_start, line_end).strip()
        self.selected_listbox = widget

    def move_task(self):
        if self.selected_task and self.selected_listbox == self.todo_listbox:
            self.done_listbox.insert("end", self.selected_task + "\n" + "-" * 40 + "\n")

            text_content = self.todo_listbox.get("1.0", "end").split("\n")
            text_content = [line for line in text_content if line.strip() != self.selected_task and line.strip() != "-" * 40]
            self.todo_listbox.delete("1.0", "end")
            self.todo_listbox.insert("1.0", "\n".join(text_content).strip())

            self.selected_task = None
            self.selected_listbox = None

    def delete_task(self):
        if self.selected_task and self.selected_listbox:
            text_content = self.selected_listbox.get("1.0", "end").split("\n")
            text_content = [line for line in text_content if line.strip() != self.selected_task and line.strip() != "-" * 40]
            self.selected_listbox.delete("1.0", "end")
            self.selected_listbox.insert("1.0", "\n".join(text_content).strip())

            self.selected_task = None
            self.selected_listbox = None


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")

        self.geometry("700x450")
        self.title("Менеджер завдань")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
