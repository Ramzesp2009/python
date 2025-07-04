import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget,
    QPushButton, QComboBox, QTextEdit, QLabel, QMessageBox, QTableWidget,
    QTableWidgetItem
)
from PyQt5.QtCore import QDate
from qt_material import apply_stylesheet, list_themes

DB_NAME = "workouts.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
            )""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            workout_id INTEGER,
            note TEXT,
            FOREIGN KEY(workout_id) REFERENCES workouts(id))""")
    conn.commit()
    conn.close()

class WorkoutApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Календар для статичних тренувань")
        self.setGeometry(100, 100, 400, 400)
        self.selected_schedule_id = None
        self.init_ui()
        self.load_workouts()
        self.update_table()


    def init_ui(self):
        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.update_table)
        layout.addWidget(QLabel("📅 Вибери дату:"))
        layout.addWidget(self.calendar)

        layout.addWidget(QLabel("🏋️‍♂️ Вибери тренування або введи нове:"))
        self.combo = QComboBox()
        self.combo.setEditable(True)
        layout.addWidget(self.combo)

        layout.addWidget(QLabel("📝 Коментар до тренування:"))
        self.note = QTextEdit()
        layout.addWidget(self.note)

        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("💾 Зберегти")
        self.edit_btn = QPushButton("✏️ Редагувати")
        self.delete_btn = QPushButton("🗑 Видалити")
        self.save_btn.clicked.connect(self.save_training)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.edit_btn)
        layout.addWidget(self.delete_btn)

        layout.addLayout(btn_layout)

        self.save_btn.clicked.connect(self.save_training)
        self.edit_btn.clicked.connect(self.edit_training)
        self.delete_btn.clicked.connect(self.delete_training)

        # Таблиця
        layout.addWidget(QLabel("📋 Тренування на вибрану дату:"))
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Назва", "Коментар", "ID"])
        self.table.setColumnHidden(2, True) # Приховуємо ID
        self.table.cellClicked.connect(self.load_selected_row)
        layout.addWidget(self.table)

        self.setLayout(layout)


    def load_workouts(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM workouts ORDER BY name")
        workouts = cursor.fetchall()
        self.combo.clear()
        for w in workouts:
            self.combo.addItem(w[0])
        conn.close()
        self.combo.setEditText("")


    def update_table(self):
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.id, w.name, s.note
            FROM schedule s
            JOIN workouts w ON s.workout_id = w.id
            WHERE s.date = ?
        """, (date,))
        records = cursor.fetchall()
        conn.close()

        self.table.setRowCount(0)
        for row_num, row_data in enumerate(records):
            self.table.insertRow(row_num)
            self.table.setItem(row_num, 0, QTableWidgetItem(row_data[1])) # Назва
            self.table.setItem(row_num, 1, QTableWidgetItem(row_data[2])) # Коментар
            self.table.setItem(row_num, 2, QTableWidgetItem(str(row_data[0]))) # ID

        self.selected_schedule_id = None


    def save_training(self):
        # спробувати потім чи можна "dd-MM-yyyy"
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        workout_name = self.combo.currentText().strip()
        note_text = self.note.toPlainText()

        if not workout_name:
            QMessageBox.warning(self, "Помилка", "Введи назву тренування")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Додати тренування в список, якщо його ще немає
        cursor.execute("INSERT OR IGNORE INTO workouts(name) VALUES(?)", (workout_name,))
        conn.commit()

        # Отримати id тренування
        cursor.execute("SELECT id FROM workouts WHERE name=?", (workout_name,))
        workout_id = cursor.fetchone()[0]

        # Додати тренування в розклад
        cursor.execute("""
            INSERT INTO schedule(date, workout_id, note) 
            VALUES(?, ?, ?)""", (date, workout_id, note_text))
        conn.commit()
        conn.close()

        self.note.clear()
        self.combo.setEditText("")
        self.load_workouts()
        self.update_table()
        QMessageBox.information(self, "Успіх", f"Тренування '{workout_name}' на {date} збережено!")


    def load_selected_row(self, row, column):
        self.selected_schedule_id = int(self.table.item(row, 2).text())
        workout_name = self.table.item(row, 0).text()
        note = self.table.item(row, 1).text()

        self.combo.setCurrentText(workout_name)
        self.note.setText(note)


    def edit_training(self):
        if self.selected_schedule_id is None:
            QMessageBox.warning(self, "Увага", "Оберіть тренування для редагування")
            return

        workout_name = self.combo.currentText().strip()
        note_text = self.note.toPlainText()

        if not workout_name:
            QMessageBox.warning(self, "Помилка", "Введи назву тренування")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Додати тренування в список, якщо його ще немає
        cursor.execute("INSERT OR IGNORE INTO workouts(name) VALUES(?)", (workout_name,))
        conn.commit()

        cursor.execute("SELECT id FROM workouts WHERE name = ?", (workout_name,))
        workout_id = cursor.fetchone()[0]

        cursor.execute("""
            UPDATE schedule
            SET workout_id = ?, note = ?
            WHERE id = ?
            """, (workout_id, note_text, self.selected_schedule_id))
        conn.commit()
        conn.close()

        self.note.clear()
        self.selected_schedule_id = None
        self.load_workouts()
        self.update_table()
        QMessageBox.information(self, "Оновлено", "Тренування оновлено!")


    def delete_training(self):
        if self.selected_schedule_id is None:
            QMessageBox.warning(self, "Увага", "Оберіть тренування для видалення")
            return

        confirm = QMessageBox.question(self, "Підтвердження", "Видалити обране тренування?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM schedule WHERE id = ?", (self.selected_schedule_id,))
        conn.commit()
        conn.close()

        self.note.clear()
        self.selected_schedule_id = None
        self.update_table()
        QMessageBox.information(self, "Видалено", "Тренування видалено")



if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = WorkoutApp()
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec_())
