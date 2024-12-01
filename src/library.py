# src/library.py

class Book:
    """
    Clase que representa un libro en la biblioteca.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        Inicializa un libro con título, autor y año de publicación.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Retorna una representación legible del libro.
        """
        return f"'{self.title}' de {self.author} ({self.year})"


class Library:
    """
    Clase que representa una biblioteca, la cual gestiona una colección de libros.
    """
    def __init__(self):
        """
        Inicializa una biblioteca vacía.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Agrega un libro a la colección.
        """
        self.books.append(book)

    def remove_book(self, title: str):
        """
        Elimina un libro de la colección por su título.
        Si no se encuentra, lanza una excepción.
        """
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        raise ValueError(f"El libro con título '{title}' no está en la biblioteca.")

    def find_books_by_author(self, author: str):
        """
        Encuentra todos los libros de un autor específico.
        """
        return [book for book in self.books if book.author == author]

    def list_books(self):
        """
        Retorna una lista de todos los libros en la colección.
        """
        return self.books
