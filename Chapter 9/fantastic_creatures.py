class FantasyCreature:
    """A simple class to represent fantasy creatures"""

    def __init__(self, name, species, magical_ability, age, friendliness="Neutral"):
        self.name = name.title()
        self.species = species.title()
        self.magical_ability = magical_ability.title()
        self.age = age
        self.friendliness = friendliness.title()

    def describe_creature(self):
        """Show details about the creature"""
        print(f"Information about '{self.name}':")
        print(f"- Species: {self.species}")
        print(f"- Magical Ability: {self.magical_ability}")
        print(f"- Age: {self.age}")
        print(f"- Friendliness: {self.friendliness}\n")

    def change_friendliness(self, new_behaviour):
        """Change the creature's friendliness"""
        self.friendliness = new_behaviour.title()
        if self.friendliness == "Neutral":
            print(f"'{self.name}' is neutral. Be careful, it might change its mood!")
        elif self.friendliness == "Friendly":
            print(f"'{self.name}' is a friendly creature. It's safe to approach.")
        else:
            print(f"'{self.name}' is an aggressive creature. Stay away!\n")


# Creating instances of the class FantasyCreature
creature1 = FantasyCreature("buckbeak", "hippogriff", "fly", 5)
creature2 = FantasyCreature("dobby", "elf", "anything", 6)
creature3 = FantasyCreature(
    "fluffy",
    "three-headed dog",
    "protect the sorcerer's stone",
    10,
)

# Calling the method describe_creature for each instance
creature1.describe_creature()
creature2.describe_creature()
creature3.describe_creature()

# Calling the method change_friendliness for each instance
creature1.change_friendliness("aggressive")
creature2.change_friendliness("friendly")
creature3.change_friendliness("neutral")
