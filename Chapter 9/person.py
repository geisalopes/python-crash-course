class Person:

    def __init__(self, name, age):
        """A simple class to represent a person"""
        self.name = name.title()
        self.age = age

    def introduce_person(self):
        """Print a message introducing the person."""
        print(f"My name is {self.name} and I'm {self.age} years old.")

    def birthday(self):
        self.age += 1


# Creating instances of the Person class
person1 = Person("geisa lopes", 40)
person2 = Person("diogo eichert", 46)
person3 = Person("vilma lopes", 70)

# Calling the method to introduce the person and then calling birthday
person1.introduce_person()
person1.birthday()
person1.introduce_person()

person2.introduce_person()
person2.birthday()
person2.introduce_person()

person3.introduce_person()
person3.birthday()
person3.introduce_person()
