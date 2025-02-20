class Character:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe_character(self):
        print(f"Name: {self.name}, Species: {self.species}\n")


class Magician(Character):
    def __init__(self, name, species, special_class):
        super().__init__(name, species)
        self.special_class = special_class

    def describe_character(self):
        # Chamando o método da classe-pai e adicionando a nova informação
        super().describe_character()
        print(f"Special Class: {self.special_class}\n")


character = Magician("Elias Thornwood", "Unknown", "Magician")
character.describe_character()
