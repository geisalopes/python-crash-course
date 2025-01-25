class Book:
    """A simple attempt to represent a book shelf"""

    def __init__(self, title, author, genre, read_status="not read yet"):
        self.title = title.title()
        self.author = author.title()
        self.genre = genre.title()
        self.read_status = read_status

    def describe_book(self):
        """A method that describe a book"""
        print("Here is the information about your book:")
        print(f"- Title: {self.title}")
        print(f"- Author: {self.author}")
        print(f"- Genre: {self.genre}")
        print(f"- Read Status: {self.read_status}\n")

    def mark_as_read(self, new_status):
        """Change the read status of the book"""
        self.read_status = new_status
        print(
            f"The read status of '{self.title}' has been updated to: {self.read_status}."
        )


# Creating the default objetcts from the class Book.
book1 = Book("divine rivals", "rebecca ross", "romantasy")
book2 = Book("fourth wing", "rebecca yarros", "fantasy")

# Creating a object with a different read_status
book3 = Book("mr. mercedes", "stephen king", "thriller", read_status="finished")

# Calling the method that describes the books
book1.describe_book()
book2.describe_book()
book3.describe_book()

# Updating the status of book 3
book3.mark_as_read("not finished yet")
