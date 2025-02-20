class Character:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe_character(self):
        print(f"Name: {self.name}, Species: {self.species}\n")


class Hero(Character):
    def __init__(self, name, species, special_ability):
        super().__init__(name, species)
        self.special_ability = special_ability

    def use_ability(self):
        print(f"{self.name} is using the power of {self.special_ability}\n")


class Villain(Character):
    def __init__(self, name, species, evil_plan):
        super().__init__(name, species)
        self.evil_plan = evil_plan

    def execute_plan(self):
        print(f"{self.name} intends to {self.evil_plan}.\n")


class Mentor(Character):
    def __init__(self, name, species, wisdom_level, advice):
        super().__init__(name, species)
        self.wisdom_level = wisdom_level
        self.advice = advice

    def give_advice(self):
        print(
            f"{self.name} with a wisdom level of {self.wisdom_level}, says: {self.advice}."
        )


character1 = Character("Morgus Thornhouse", "Capricorn")
character1.describe_character()

character2 = Hero("Cecilia Goldenleaf", "Aquariana", "Talk to the Moon Dragon")
character2.describe_character()
character2.use_ability()

character3 = Villain("Karowmor Hagtrah", "Scorpion", "Steal the Magic Horses")
character3.describe_character()
character3.execute_plan()

character4 = Mentor(
    "Marius Chanceget", "Leon", 500, "You should focus on get back one horse at time"
)
character4.describe_character()
character4.give_advice()
