class User:
    """A simple class to describe a user"""

    def __init__(self, first_name, last_name, username, email):
        """Defining the user's attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def describe_user(self):
        """A methos to describe the user"""
        print(
            f"User's Information: Name: {self.first_name} {self.last_name}, Username: {self.username}, Email: {self.email}"
        )

    def greet_user(self):
        """A method to welcome the user"""
        print(f"Welcome {self.first_name} {self.last_name}.\n")


geisa = User("geisa", "lopes", "geisalopes", "geisa84@gmail")
geisa.describe_user()
geisa.greet_user()

diogo = User("diogo", "eichert", "dgeichert", "deichert@gmail")
diogo.describe_user()
diogo.greet_user()
