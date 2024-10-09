# First Option

# prompt = "\nPlease enter your favorite toppings: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# toppings = ""
# while toppings != "quit":
#     toppings = input(prompt)

#     if toppings != "quit":
#         print(toppings)


# Second Option

# prompt = "\nPlease enter your favorite toppings: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# active = True
# while active:
#     toppings = input(prompt)

#     if toppings == "quit":
#         active = False
#     else:
#         print(toppings)


# Third Option
prompt = "\nPlease enter your favorite toppings: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)

    if toppings == "quit":
        break
    else:
        print(f"\nI'll add {toppings} to your pizza.")
