# Create an empty list to store the pets in
pets = []

# Create a dictionary of pets

pet = {"name": "gurizinho", "kind": "cat", "owner": "vilma", "eats": "agradinho"}
pets.append(pet)

pet = {"name": "tuquinha", "kind": "dog", "owner": "geisa", "eats": "cat poop"}
pets.append(pet)

pet = {"name": "tugui", "kind": "turtle", "owner": "daiana", "eats": "turtle food"}
pets.append(pet)

# Display information about each pet
for pet in pets:
    print("\nHere's what I know  about " + pet["name"].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
