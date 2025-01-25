class Book:
    """A simple class to represent a book."""

    def __init__(self, title, author, pages):
        self.title = title.title()
        self.author = author.title()
        self.pages = pages
        self.pages_read = 0  # Inicialmente, nenhuma página foi lida.

    def calculate_percentage_read(self):
        """Calculate and return the percentage of the book read."""
        return (self.pages_read / self.pages) * 100

    def describe_book(self):
        """Show details about the book, including pages read."""
        percentage_read = self.calculate_percentage_read()
        print(f"- Book title: {self.title}")
        print(f"- Author: {self.author}")
        print(f"- Number of pages: {self.pages}")
        print(f"- Pages read: {self.pages_read} ({percentage_read:.1f}% completed)\n")

    def update_pages_read(self, pages_read):
        """Update the number of pages read and show the new progress."""
        self.pages_read += pages_read
        percentage_read = self.calculate_percentage_read()
        print(
            f"- Pages read so far: {self.pages_read} ({percentage_read:.1f}% completed)\n"
        )


# Testando o código
book = Book("happy place", "henry emily", 357)

# Mostrando informações iniciais
book.describe_book()

# Atualizando o número de páginas lidas
print("*Atualizando o número de páginas lidas...\n")
book.update_pages_read(50)
