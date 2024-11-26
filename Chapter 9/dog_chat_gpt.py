class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe_dog(self):
        print(f"The dog's name is: {self.name}.")
        print(f"The dog's breed is: {self.breed}.")

    def bark(self):
        print(f"Woof! I'm {self.name}!")


my_dog = Dog("Juju", "Leãozinho")
my_dog.describe_dog()
my_dog.bark()
