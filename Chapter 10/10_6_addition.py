try:
    number_one = int(input("Give me one number. "))
    number_two = int(input("Give me another number. "))
except ValueError:
    print("Please, give a valid number.")
else:
    numbers = number_one + number_two
    print(f"The sum of the numbers is: {numbers}.")
