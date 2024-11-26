class Pet:

    def __init__(self, name, species):
        """A simple class about a pet"""
        self.name = name.title()
        self.species = species
        self.age = 0

    def describe_pet(self):
        """Describes the informations about the pet"""
        print("Here is the pet's information: ")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years old.")

    def set_age(self, age):
        if age >= 1:
            self.age = age
            print(f"The age of {self.name} was set for {self.age} years old")
        else:
            print("You must choose a valid age for your pet!")

    def increment_age(self, increment):
        new_age = self.age + increment
        if new_age > 20:
            print(f"Maximum age limit reached for {self.name}!")
            self.age = 20
        else:
            self.age = new_age
            print(f"{self.name} is now {self.age} years old.")


my_pet = Pet("kuki", "dog")
my_pet.describe_pet()
my_pet.set_age(3)
my_pet.increment_age(12)
my_pet.increment_age(12)
