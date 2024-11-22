class Bookshelf:
    """A class representing a library"""

    def __init__(self):
        self.books_read = 0

    def set_books_read(self, quantity):
        self.books_read = quantity

    def increment_books_read(self, quantity):
        self.books_read += quantity


my_shelf = Bookshelf()

print(f"Books read: {my_shelf.books_read}")

my_shelf.set_books_read(5)
print(f"Books read: {my_shelf.books_read}")

my_shelf.increment_books_read(3)
print(f"Books read: {my_shelf.books_read}")
