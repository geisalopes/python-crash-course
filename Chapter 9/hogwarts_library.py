class LibraryUser:

    def __init__(self, first_name, last_name, house):
        """Represent a user of the Hogwarts library."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.house = house.title()
        self.books_checked_out = 0  # Loaned books start in 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nUser:")
        print(f"- Name: {self.first_name} {self.last_name}")
        print(f"- House: {self.house}")
        print(f"- Books checked out: {self.books_checked_out}")

    def increment_books(self):
        """Increment the number of books checked out."""
        self.books_checked_out += 1
        print(f"Books loaded: {self.books_checked_out}")

    def reset_books(self):
        """Reset the number of books checked out to 0."""
        self.books_checked_out = 0
        print(
            f"{self.first_name} returned all books. Reseting the numbers of books loaded..."
        )
        print(f"Books loaded: {self.books_checked_out}")


class Librarian(LibraryUser):
    """A librarian with special privileges at Hogwarts library."""

    def __init__(self, first_name, last_name, house):
        """Initialize the librarian."""
        super().__init__(first_name, last_name, house)

        # A librarian has a list of privileges
        self.privileges = Privileges()

    def assign_privileges(self, privileges):
        """Assign privileges to the librarian."""
        self.privileges.privileges_list = privileges


class Privileges:
    """A class to store a librarian's privileges."""

    def __init__(self, privileges=[]):
        self.privileges_list = privileges

    def show_privileges(self, librarian_name):
        "Display the librarian's privileges"
        print(f"\n{librarian_name}'s privileges: ")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f"- {privilege}")
        else:
            print("- This librarian has no special privileges.")


user = LibraryUser("Hermione", "Granger", "Gryffindor")
user.describe_user()
user.increment_books()
user.increment_books()
user.reset_books()


# Creating a librarian and adding privileges
librarian = Librarian("Madam", "Pince", "Hogwarts")
librarian.describe_user()

# Addind privileges
librarian.assign_privileges(
    ["can add books", "can remove books", "can manage library budget"]
)

# Showing privileges
librarian.privileges.show_privileges("Madam Pince")
