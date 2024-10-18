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
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nHere is the informations about the user {self.username}:")
        print(
            f"Age: {self.age} years old, Location: {self.location}, Hobby: {self.hobby}"
        )

    def greet_user(self):
        print(f"\nHello, {self.username}! Welcome on board!\n")

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login attempts to 0"""
        self.login_attempts = 0


user_one = User("Geisa", "Lopes", 40, "Berlin", "drawing")
user_one.describe_user()
user_one.greet_user()

print("\nMaking 3 login attempts...")
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(f"  Login attempts: {user_one.login_attempts}")

print("Reseting login attempts...")
user_one.reset_login_attempts()
print(f"   Login attempts: {user_one.login_attempts}")
