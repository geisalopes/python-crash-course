class Cafe:
    """A class that represents a favorite cafe"""

    def __init__(self, name, location):
        self.name = name.title()
        self.location = location.title()
        self.rating = 0

    def describe_cafe(self):
        """A simple method to describe the caf'e and location"""
        print(f"The cafe {self.name} is located in {self.location}")

    def rate_cafe(self, rating):
        """A method to define the rating directly"""
        if self.rating <= 5:
            self.rating = rating
            print(f"The rate of the cafe {self.name} is {self.rating}")
        else:
            print("Error: Rating must be btween 0 and 5.")

    def improve_rating(self, increment):
        """Improve the rating by a given value"""
        new_rating = self.rating + increment
        if new_rating > 5:  # Limit the maximum rate to 5
            print("You can't give more than 5. Setting rating to the maximum (5).")
            self.rating = 5
        else:
            self.rating = new_rating
            print(f"The rate of the cafe {self.name} is {self.rating}")


my_favorite_cafe = Cafe("monkey mind", "moabit")
my_favorite_cafe.describe_cafe()
my_favorite_cafe.rate_cafe(3)
my_favorite_cafe.improve_rating(2)
my_favorite_cafe.improve_rating(3)  # Try to increase to note beyond five
