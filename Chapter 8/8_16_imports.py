print("First Option")
import describing_pets

describing_pets.describe_pet(pet_name="willie")

print("\nSecond Option")
from describing_pets import describe_pet

describe_pet(pet_name="willie")

print("\nThird Option")
from describing_pets import describe_pet as dp

dp(pet_name="willie")

print("\nFourth Option")
import describing_pets as dpts

dpts.describe_pet(pet_name="willie")

print("\nFifth Option")
from describing_pets import *

describe_pet(pet_name="willie")
