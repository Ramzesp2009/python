from pathlib import Path

# Шлях до файлу
file_path = Path("D:\Coding Space\Python\Sport_Notebook\workout_tracker_2.py")

# Основний код PyQt-додатку (укрочено до прикладу)
code = '''
import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QCalendarWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTextEdit, QPushButton, QComboBox, QMessageBox, QTableWidget,
    QTableWidgetItem
)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QTextCharFormat, QColor, QBrush

DB_NAME = "workouts.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    c.execute("CREATE TABLE IF NOT EXISTS schedule (id INTEGER PRIMARY KEY, date TEXT, workout_id INTEGER, note TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)")
    conn.commit()
    conn.close()

class WorkoutApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Календар для статичних тренувань")
        self.workout_colors = {
            "Кардіо": "#ff5e5e",
            "Сила": "#5e9cff",
            "Йога": "#6effd2",
            "Відпочинок": "#cccccc",
            "Інше": "#ffaaff"
        }
        self.current_theme = self.load_saved_theme()
        self.init_ui()
        self.load_workouts()
        self.update_table()
        self.update_calendar_colors()
        if self.current_theme == "dark":
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def init_ui(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.update_table)
        left_layout.addWidget(QLabel("📅 Вибери дату:"))
        left_layout.addWidget(self.calendar)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["НАЗВА", "КОМЕНТАР"])
        left_layout.addWidget(QLabel("📋 Розклад на обрану дату:"))
        left_layout.addWidget(self.table)

        self.new_input = QLineEdit()
        self.new_input.setPlaceholderText("Нове тренування")
        self.combo = QComboBox()
        self.combo.setEditable(False)

        self.note = QTextEdit()
        self.note.setPlaceholderText("Коментар до тренування")

        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("💾 ЗБЕРЕГТИ")
        self.save_btn.clicked.connect(self.save_training)
        self.edit_btn = QPushButton("✏️ РЕДАГУВАТИ")
        self.edit_btn.clicked.connect(self.edit_training)
        self.delete_btn = QPushButton("🗑 ВИДАЛИТИ")
        self.delete_btn.clicked.connect(self.delete_training)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)

        self.theme_btn = QPushButton("🌗 Змінити тему")
        self.theme_btn.clicked.connect(self.toggle_theme)

        right_layout.addWidget(QLabel("🏋️‍♂️ Введи нове тренування:"))
        right_layout.addWidget(self.new_input)
        right_layout.addWidget(QLabel("📂 Вибери збережене тренування:"))
        right_layout.addWidget(self.combo)
        right_layout.addWidget(QLabel("📝 Коментар:"))
        right_layout.addWidget(self.note)
        right_layout.addLayout(btn_layout)
        right_layout.addWidget(self.theme_btn)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

    def save_training(self):
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        new_name = self.new_input.text().strip()
        workout_name = new_name if new_name else self.combo.currentText().strip()
        note_text = self.note.toPlainText()

        if not workout_name:
            QMessageBox.warning(self, "Помилка", "Введи назву тренування")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM workouts WHERE name = ?", (workout_name,))
        result = cursor.fetchone()
        if result:
            workout_id = result[0]
        else:
            cursor.execute("INSERT INTO workouts(name) VALUES(?)", (workout_name,))
            conn.commit()
            workout_id = cursor.lastrowid

        cursor.execute("INSERT INTO schedule(date, workout_id, note) VALUES(?, ?, ?)", (date, workout_id, note_text))
        conn.commit()
        conn.close()

        self.note.clear()
        self.new_input.clear()
        self.load_workouts()
        self.update_table()
        self.update_calendar_colors()
        QMessageBox.information(self, "Успіх", f"Тренування '{workout_name}' на {date} збережено!")

    def edit_training(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Увага", "Оберіть запис для редагування.")
            return

        name = self.table.item(row, 0).text()
        note = self.note.toPlainText()
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM workouts WHERE name = ?", (name,))
        workout_id = cursor.fetchone()[0]
        cursor.execute("UPDATE schedule SET note=? WHERE date=? AND workout_id=?", (note, date, workout_id))
        conn.commit()
        conn.close()

        self.update_table()
        self.update_calendar_colors()
        QMessageBox.information(self, "Успіх", "Коментар оновлено!")

    def delete_training(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Увага", "Оберіть запис для видалення.")
            return

        name = self.table.item(row, 0).text()
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM workouts WHERE name=?", (name,))
        workout_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM schedule WHERE date=? AND workout_id=?", (date, workout_id))
        conn.commit()
        conn.close()

        self.update_table()
        self.update_calendar_colors()
        QMessageBox.information(self, "Успіх", "Тренування видалено.")

    def load_workouts(self):
        self.combo.clear()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM workouts ORDER BY name")
        workouts = cursor.fetchall()
        conn.close()
        for (name,) in workouts:
            self.combo.addItem(name)

    def update_table(self):
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT w.name, s.note FROM schedule s
            JOIN workouts w ON s.workout_id = w.id
            WHERE s.date = ?
        """, (date,))
        rows = cursor.fetchall()
        conn.close()
        self.table.setRowCount(len(rows))
        for i, (name, note) in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(note or ""))

    def update_calendar_colors(self):
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.date, w.name FROM schedule s
            JOIN workouts w ON s.workout_id = w.id
        """)
        records = cursor.fetchall()
        conn.close()
        for date_str, workout_name in records:
            qdate = QDate.fromString(date_str, "yyyy-MM-dd")
            color = self.workout_colors.get("Інше")
            for key in self.workout_colors:
                if key.lower() in workout_name.lower():
                    color = self.workout_colors[key]
                    break
            fmt = QTextCharFormat()
            fmt.setBackground(QBrush(QColor(color)))
            self.calendar.setDateTextFormat(qdate, fmt)

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.set_light_theme()
            self.current_theme = "light"
        else:
            self.set_dark_theme()
            self.current_theme = "dark"
        self.save_theme(self.current_theme)

    def set_dark_theme(self):
        dark_stylesheet = """
        QWidget { background-color: #2b2b2b; color: #f0f0f0; font-size: 14px; }
        QCalendarWidget QWidget { background-color: #3c3f41; color: #f0f0f0; }
        QTextEdit, QComboBox, QLineEdit, QTableWidget {
            background-color: #3c3f41; color: #ffffff; border: 1px solid #5c5c5c;
        }
        QPushButton {
            background-color: #44475a; color: #ffffff;
            border: 1px solid #6272a4; padding: 6px; border-radius: 5px;
        }
        QPushButton:hover { background-color: #6272a4; }
        QTableWidget::item:selected { background-color: #44475a; color: #ffffff; }
        """
        self.setStyleSheet(dark_stylesheet)

    def set_light_theme(self):
        self.setStyleSheet("")

    def save_theme(self, theme):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO settings(key, value) VALUES (?, ?)", ("theme", theme))
        conn.commit()
        conn.close()

    def load_saved_theme(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM settings WHERE key = ?", ("theme",))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else "dark"

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = WorkoutApp()
    window.show()
    sys.exit(app.exec_())
'''

# Зберігаємо файл
file_path.write_text(code, encoding="utf-8")
file_path.name
