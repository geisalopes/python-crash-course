class Book:
    """A class that represents a book"""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        """display informaiton about a specific book"""
        print(f"The book {self.title} was written by {self.author}.")


class FantasyBook(Book):
    """A class that inherits information from the Book class"""

    def __init__(self, title, author, magic_system):
        super().__init__(title, author)
        self.magic_system = magic_system

    def describe_magic(self):
        print(f"Book: {self.title}, Magic System: {self.magic_system} ")


# Creating an object to represent the Book class
book1 = Book("Check & Mate", "Ali Hazelwood")
book1.describe_book()

book2 = FantasyBook("Harry Potter", "J K Rowling", "Wand-based spellcasting")
book2.describe_book()
book2.describe_magic()
