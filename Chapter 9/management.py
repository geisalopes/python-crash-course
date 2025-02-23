class StoreChain:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def describe_chain(self):
        print(f"{self.name} operates in {self.country}.")
