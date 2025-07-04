# Use utf-8 support via `fpdf2` instead of older `fpdf`
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Angular: Структурований конспект для вивчення", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 120)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

# Use a Unicode-supporting font
pdf = PDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", "", 12)

content = [
    ("1. Основи TypeScript", """
- Типи, інтерфейси, класи, generics
- Union types, enum, type aliases
- Модулі та імпорти/експорти
- Практика: невеликий калькулятор на TypeScript
"""),
    ("2. Основи Angular", """
- Архітектура: компоненти, шаблони, модулі, сервіси
- Angular CLI: створення проекту, структура папок
- Data binding: interpolation {{ }}, property [ ], event ( ), two-way [(ngModel)]
- Директиви: *ngIf, *ngFor, [ngClass], [ngStyle]
"""),
    ("3. Сервіси та Dependency Injection", """
- Створення сервісів через CLI
- Впровадження сервісів у компоненти
- Життєвий цикл сервісів (Singleton, @Injectable)
"""),
    ("4. Маршрутизація", """
- Налаштування маршрутів у AppRoutingModule
- Використання routerLink, router-outlet
- Передача параметрів через URL
"""),
    ("5. HTTP-запити", """
- Імпорт HttpClientModule
- GET, POST, PUT, DELETE
- Обробка помилок: catchError, tap
"""),
    ("6. Форми", """
- Template-driven Forms: ngForm, ngModel
- Reactive Forms: FormGroup, FormControl, FormBuilder
- Валідація: required, minlength, custom validators
"""),
    ("7. RxJS", """
- Observables, Subjects, BehaviorSubject
- Оператори: map, filter, switchMap, debounceTime
- unsubscribe та takeUntil для уникнення утечок пам’яті
"""),
    ("8. Практичний проект", """
- CRUD-застосунок: список задач / нотаток
- Використання форми, маршрутизації, HTTP-запитів
- Використання Angular Material або Bootstrap для UI
"""),
    ("Корисні посилання", """
- https://angular.io/start — офіційний стартовий гайд
- https://angular.io/tutorial — Tour of Heroes (навчальний проект)
- https://rxjs.dev/guide/overview — RxJS офіційна документація
- https://www.typescriptlang.org/docs/ — Документація по TypeScript
""")
]

for title, body in content:
    pdf.set_font("DejaVu", "", 12)
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf_path = "/mnt/data/Angular_Konspekt.pdf"
pdf.output(pdf_path)
pdf_path
