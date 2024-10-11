# Using a function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# This is a infinite loop!
# while True:
#     print(f"\nPlease tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")


# Now the same code, but using break statement to exit the loop


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name: ")
    print("(enter 'q'at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
