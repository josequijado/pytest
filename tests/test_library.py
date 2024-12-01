# test_library.py
import sys
import os
import pytest
from src.library import Book, Library

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

@pytest.fixture
def sample_library():
    """
    Fixture que configura una biblioteca con algunos libros de ejemplo.
    """
    library = Library()
    library.add_book(Book("Cien años de soledad", "Gabriel García Márquez", 1967))
    library.add_book(Book("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985))
    library.add_book(Book("1984", "George Orwell", 1949))
    return library


def test_add_book(sample_library):
    """
    Prueba que se pueda agregar un libro a la biblioteca.
    """
    new_book = Book("El Principito", "Antoine de Saint-Exupéry", 1943)
    sample_library.add_book(new_book)
    assert len(sample_library.books) == 4
    assert sample_library.books[-1].title == "El Principito"


def test_remove_book(sample_library):
    """
    Prueba que se pueda eliminar un libro por su título.
    """
    sample_library.remove_book("1984")
    assert len(sample_library.books) == 2
    assert all(book.title != "1984" for book in sample_library.books)


def test_remove_nonexistent_book(sample_library):
    """
    Prueba que intentar eliminar un libro que no existe lanza una excepción.
    """
    with pytest.raises(ValueError, match="El libro con título 'No existe' no está en la biblioteca."):
        sample_library.remove_book("No existe")


def test_find_books_by_author(sample_library):
    """
    Prueba que se pueden encontrar libros por el autor.
    """
    books = sample_library.find_books_by_author("Gabriel García Márquez")
    assert len(books) == 2
    assert all(book.author == "Gabriel García Márquez" for book in books)


def test_list_books(sample_library):
    """
    Prueba que se pueda listar todos los libros en la biblioteca.
    """
    books = sample_library.list_books()
    assert len(books) == 3
    titles = [book.title for book in books]
    assert "Cien años de soledad" in titles
    assert "1984" in titles
    assert "El amor en los tiempos del cólera" in titles
