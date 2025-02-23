class Book:
    """Represents a Book"""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"{self.title} is written by {self.author}")


class Librarian:

    def __init__(self, name, library_name):
        self.name = name
        self.library_name = library_name

    def describe_librarian(self):
        print(f"{self.name} works at the {self.library_name} library.")
