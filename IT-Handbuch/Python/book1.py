class Book:
    # Konstruktor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
     # String-Darstellung
    def __str__(self):
        return f"{self.author}: '{self.title}' ({self.year})"

# Hauptprogramm
if __name__ == "__main__":
    book1 = Book("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
    book2 = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 1997)
    print(book1)
    print(book2)