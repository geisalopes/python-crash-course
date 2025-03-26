print("Enter 'q' at any time to quit.\n")

while True:
    try:
        number_one = input("\nGive me a number. ")
        if number_one == "q":
            break

        number_one = int(number_one)

        number_two = input("\nGive me another number. ")
        if number_two == "q":
            break

        number_two = int(number_two)

    except ValueError:
        print("Please, give a valid number.")
    else:
        numbers = number_one + number_two
        print(f"The sum of the numbers is: {numbers}.")
