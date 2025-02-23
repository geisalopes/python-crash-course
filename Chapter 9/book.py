class Book:
    """Represents a Book"""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"{self.title} is written by {self.author}")
