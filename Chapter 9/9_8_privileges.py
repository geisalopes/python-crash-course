class User:
    """Represent a simple profile"""

    def __init__(self, first_name, last_name, age, location, hobby):
        """Initialize the user."""
        self.first = first_name
        self.last = last_name
        self.username = self.first + " " + self.last
        self.age = age
        self.location = location
        self.hobby = hobby

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nHere is the informations about the user {self.username}:")
        print(f"Age: {self.age} years old")
        print(f"Location: {self.location}")
        print(f"Hobby: {self.hobby}")

    def greet_user(self):
        print(f"\nHello, {self.username}! Welcome on board!\n")


class Admin(User):
    """A class to define a admin."""

    def __init__(self, first_name, last_name, age, location, hobby):
        """Initialize attributes of the parent class."""
        super().__init__(
            first_name,
            last_name,
            age,
            location,
            hobby,
        )
        """Initialize  an empty set of privileges"""
        self.privileges = Privileges()


class Privileges:
    """A class to store admin's  privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


diogo = Admin("Diogo", "Eichert", 46, "Berlin", "likes comics")
diogo.describe_user()

diogo.privileges.show_privileges()

print("\nAdding privileges...")
diogo_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]

diogo.privileges.privileges = diogo_privileges
diogo.privileges.show_privileges()
