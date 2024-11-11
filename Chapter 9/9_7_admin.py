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
        """Then initialize attributes specific to an admin"""
        super().__init__(
            first_name,
            last_name,
            age,
            location,
            hobby,
        )
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin("Diogo", "Eichert", 46, "Berlin", "likes comics")
admin_user.describe_user()
admin_user.show_privileges()
