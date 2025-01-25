class Book:
    """A simple attempt to represent a book"""

    def __init__(self, title, author, year):
        """Initialize attributes to describe a book"""
        self.title = title  # THe title of the book
        self.author = author  # The author of the book
        self.year = year  # The year that the book was published
        self.pages_read = 0  # The number of read pages start in 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        # Return a string with information of the book in the format "Title per Author (Year)"
        long_name = f"{self.title} by {self.author} ({self.year})"
        return long_name.title()

    def read_pages(self):
        """Print a statement showing the book's progress"""
        # Print how many pages were readed so far.
        print(f"This book has {self.pages_read} pages read so far.")

    def update_pages(self, pages):
        """Set the pages read to the given value"""
        # Update the number of read pages, if the value is bigger or equal to the actual.
        if pages >= self.pages_read:
            self.pages_read = pages
        else:
            print("You can't reduce the number of pages already read!")

    def increment_pages(self, pages):
        """Add the given number to the pages read."""
        # Add a number of pages to the actual progress
        self.pages_read += pages


class LibraryCard:
    """A simple attempt to model a library card"""

    def __init__(self, max_books=5):
        """Initialize the library card's attributes."""
        self.max_books = max_books  # Limit of books that the card allow to borrow.
        self.books_borrowed = 0  # Amount of currently borrowed books.

    def describe_card(self):
        """Print a statement describing the library card."""
        # Show the limit of allowed borrows.
        print(f"This card allows borrowing up to {self.max_books} books at a time.")

    def borrow_book(self):
        """Simulate borrowing a book."""
        # Simulate the borrow of a book, verifying the limit.
        if self.books_borrowed < self.max_books:
            self.books_borrowed += 1
            print(
                f"You borrowed a book. {self.max_books - self.books_borrowed} borrow(s) left."
            )
        else:
            print("You've reached your borrowing limit!")

    def return_book(self):
        """Simulate returning a book."""
        # Simulate the returning of a book
        if self.books_borrowed > 0:
            self.books_borrowed -= 1
            print(
                f"You returned a book. {self.max_books - self.books_borrowed} borrow(s) left."
            )
        else:
            print("You have no book to return!")


class Library:
    """Represent a library, specific to managing books and memberships."""

    def __init__(self, name, location):
        """Initialize the attributes of a library."""
        self.name = name  # Library's name
        self.location = location  # Library's location
        self.card = LibraryCard()  # Each library has a associated card

    def add_book(self, book):
        """Add a book to the library's collection."""
        print(
            f"The book '{book.get_descriptive_name()}' was added to the library collection."
        )

    def describe_library(self):
        """Provide details about the library."""
        print(f"Welcome to {self.name} Library located in {self.location}.")


# First Message
print("Welcome to the Library System!")

# Creating a book
my_book = Book("Lessons in Chemistry", "Bonnie H", 2023)
print(my_book.get_descriptive_name())  # Show the formatted title

# Creating a library
city_library = Library("Humboldt Library", "Berlin")
city_library.describe_library()  # Show information about the library

# Adding books to the library
city_library.add_book(my_book)

# Using the library's card
print(f"\nChecking the library card:")
city_library.card.describe_card()  # Show the card's limit

print("\nBorrowing a book:")
city_library.card.borrow_book()  # Borrow a book

print("\nReturning a book:")
city_library.card.return_book()  # Return the book
