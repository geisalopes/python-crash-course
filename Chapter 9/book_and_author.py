class Author:
    """A simple Author for a book"""

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def describe_author(self):
        """Display a message about the author"""
        print(f"The author of this book is {self.name}, born in {self.birth_year}.")

    def get_age(self, current_year):
        """Display the author's age based on the current year."""
        age = current_year - self.birth_year
        print(f"{self.name} would be approximately {age} years old today.")


class Book:
    """Represents specific aspects of a book."""

    def __init__(self, title, genre, publication_year):
        """Initialize the books' attributes."""
        self.title = title
        self.genre = genre
        self.publication_year = publication_year
        self.author = None

    def describe_book(self):
        """Display information about a book."""
        print(
            f"{self.title}, a book of the genre {self.genre}, published in {self.publication_year}."
        )


machado_de_assis = Author("Machado de Assis", 1839)
my_book = Book("Dom Casmurro", "Novel", 1899)
my_book.author = machado_de_assis

my_book.describe_book()
my_book.author.describe_author()
my_book.author.get_age(2025)

tolkien = Author("Tolkien", 1920)
my_book2 = Book("Senhor dos Aneis", "Fantasy", 1980)
my_book2.author = tolkien

my_book2.describe_book()
my_book2.author.describe_author()
my_book2.author.get_age(2025)
