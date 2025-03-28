# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet("hamster", "harry")
# describe_pet("dog", "willie")


"""Now we will write the same code, bus using Keyord Arguments, 
so you don't need to worry about the position os the parameters and arguments"""

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet(pet_name="harry", animal_type="hamster")

"""Default Values"""


def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="willie")

"""Equivalent Functin Calls"""
# def describe_pet(pet_name, animal_type= 'dog'):

# # A dog named Willie
# describe_pet('willie')
# describe_pet(pet_name= 'willie')

# # A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name= 'harry', animal_type= 'hamster')
# describe_pet(animal_type= 'hamster', pet_name= 'harry')
