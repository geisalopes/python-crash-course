class Pet:
    """A simple class to represent a pet."""

    def __init__(self, name, animal_type, age, health_status="healthy"):
        self.name = name
        self.type = animal_type
        self.age = age
        self.health_status = health_status

    def describe_pet(self):
        """Print information about the pet."""
        print("\nInformation about your pet...")
        print(f"This is {self.name}, a {self.type} that is {self.age} years old. ")
        print(f"Current health status: {self.health_status}")

    def update_health_status(self, new_status):
        """Update the health status of the pet."""
        self.health_status = new_status
        print(f"Health status of {self.name} updated to: {self.health_status}")

    # def birthday(self):
    #     self.age += 1
    #     print(f"{self.name} is now {self.age} years old.")

    # def speak(self, sound):
    #     print(f"{self.name} says {sound}!")


# dog = Pet("Lassie", "dog", 5)
# dog.describe_pet()
# dog.birthday()
# dog.speak("woof")

# Criando instâncias com o valor padrão de saúde
dog = Pet("Buddy", "dog", 4)
cat = Pet("Mimi", "cat", 2)

# Criando uma instância com um valor personalizado para saúde
rabbit = Pet("Fluffy", "rabbit", 1, health_status="sick")

# Chamando o método describe_pet para cada instância
dog.describe_pet()
cat.describe_pet()
rabbit.describe_pet()

# Atualizando o estado de saúde do coelho
rabbit.update_health_status("healthy")
