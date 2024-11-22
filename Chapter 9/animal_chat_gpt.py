class Animal:
    """A class that print the name of an animal"""

    def __init__(self, name):
        """Here I define the name of the animal"""
        self.name = name

    def show_name(self):
        """Here I show the name of the animal"""
        print(f"The name of the animal is {self.name}")


# Create an instance of the class animal
my_pet = Animal("Kuki")

my_pet.show_name()
