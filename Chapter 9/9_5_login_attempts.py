class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


geisa = User("geisa", "lopes", "g_lopes", "g_lopes@example.com", "berlin")
geisa.describe_user()
geisa.greet_user()

print(f"Login attemmpts... ")
geisa.increment_login_attempts()
geisa.increment_login_attempts()
geisa.increment_login_attempts()
geisa.increment_login_attempts()
print(f"Total of login attempts: {geisa.login_attempts}")

print("\nResetting Login Attempts...")
geisa.reset_login_attempts()
print(f"Total of login attempts: {geisa.login_attempts}")
