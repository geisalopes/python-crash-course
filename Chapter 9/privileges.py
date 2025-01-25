class Student:
    """Represent a simple student profile at Hogwarts."""

    def __init__(self, first_name, last_name, username, house, year):
        """Initialize the student."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.house = house.title()
        self.year = year
        self.attendance = 0

    def describe_student(self):
        """Display a summary of the student's information."""
        print(f"\n {self.first_name} {self.last_name}")
        print(" Username: " + self.username)
        print(" House: " + self.house)
        print(" Year: " + str(self.year))

    def greet_student(self):
        """Display a personalized greeting to the student."""
        print(f"\n Welcome back to Hogwarts, {self.username}!")

    def increment_attendance(self):
        """Increment the value of attendance."""
        self.increment_attendance += 1

    def reset_attendance(self):
        """Reset attendance to 0."""
        self.attendance = 0


class Professor(Student):
    """A student who is also a professor at Hogwarts with special privileges."""

    def __init__(self, first_name, last_name, username, house, year):
        """Initialize the professor."""
        super().__init__(first_name, last_name, username, house, year)

        # Initialize an empty list of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store a professor's privileges at Hogwarts."""

    def __init__(self, privileges=[]):
        self.privileges_list = privileges

    def show_privileges(self):
        print("\nProfessor Privileges:")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f"-  {privilege}")
        else:
            print("- This professor has no special privileges.")


# Creating a teacher
professor_snape = Professor("Severus", "Snape", "slytherin_master", "Slytherin", 7)
professor_snape.describe_student()

# Show privileges before adding.
professor_snape.privileges.show_privileges()

# Adding privileges to the teacher
professor_privileges = [
    "can teach Potions",
    "can administer detentions",
    "can access the Restricted Section of the library",
]


professor_snape.privileges.privileges_list = professor_privileges
professor_snape.privileges.show_privileges()
