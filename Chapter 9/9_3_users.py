class User:
    """Creating a simple class to store informations about users"""

    def __init__(self, first_name, last_name, age, location, hobby):
        """Giving name and last name attributes."""
        self.first = first_name
        self.last = last_name
        self.username = self.first + " " + self.last
        self.age = age
        self.location = location
        self.hobby = hobby

    def describe_user(self):
        """Creating a summary of the user's information"""
        print(
            f"Here is the informations about the user {self.username}: {self.age} years old, from {self.location}, favorite hobby: {self.hobby}"
        )

    def greet_user(self):
        print(f"Hello, {self.username}! Wellcome on board!\n")


user_one = User("Geisa", "Lopes", 40, "Berlin", "drawing")
user_one.describe_user()
user_one.greet_user()
