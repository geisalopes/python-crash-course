class Book:

    def __init__(self, title, author, pages):
        "A simple class representing information about a book."
        self.title = title.title()
        self.author = author.title()
        self.pages = pages
        self.pages_read = 0

    def describe_book(self):
        "A simple method that is called to describe the book"
        print("Information about this book:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of pages: {self.pages}")
        print(f"\nNumber of pages read so far: {self.pages_read}")

    def update_pages_read(self, pages_increment):
        """A method that updates the number of pages read so far"""
        new_total = self.pages_read + pages_increment
        if new_total > self.pages:
            print(
                f"\nThis books has a maximum of {self.pages} pages. You cant' read more than that."
            )
        else:
            self.pages_read = new_total
            print(f"Number of pages read so far: {self.pages_read}")

    def reset_pages_read(self):
        """Reset the number of pages read."""
        self.pages_read = 0
        print("\nI'll start the book again.")
        print(f"Number of pages read so far: {self.pages_read}")


my_book = Book("never", "ken follet", 567)
my_book.describe_book()

my_book.update_pages_read(56)
my_book.update_pages_read(147)
my_book.update_pages_read(238)
my_book.update_pages_read(376)
my_book.reset_pages_read()
