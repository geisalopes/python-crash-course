class Planet:

    def __init__(self, name, distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun

    def describe_planet(self):
        print(f"{self.name} is {self.distance_from_sun} million km away from the Sun.")
