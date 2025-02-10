class Book:
    """A simple class to represent a book."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe_book(self):
        """This method shows information about the book"""
        print(f"Here is the information about your book:")
        print(f" Title: {self.title}")
        print(f" Author: {self.author}")
        print(f" Pages: {self.pages}\n")


# Creating a object to represent a book
harrypotter = Book("Harry Potter e o Enigma do Principe", "J.K. Rowling", 567)
harrypotter.describe_book()

# Setting a different value directly to the number of pages
harrypotter.pages = 600
harrypotter.describe_book()
