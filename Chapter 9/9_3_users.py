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
        print(
            f"Age: {self.age} years old, Location: {self.location}, Hobby: {self.hobby}"
        )

    def greet_user(self):
        print(f"\nHello, {self.username}! Welcome on board!\n")


user_one = User("Geisa", "Lopes", 40, "Berlin", "drawing")
user_one.describe_user()
user_one.greet_user()
