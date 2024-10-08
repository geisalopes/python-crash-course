# prompt = "\nPlease enter your favorite toppings: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     toppings = input(prompt)
#     if toppings == "quit":
#         break
#     else:
#         print(f"\n I will add {toppings} to your pizza.")


# prompt = "\nPlease enter your favorite toppings: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# active = True
# while active:
#     toppings = input(prompt)
#     if toppings == "quit":
#         active = False
#     else:
#         print(f"\n I will add {toppings} to your pizza.")


prompt = "\nPlease enter your favorite toppings: "
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    toppings = input(prompt)
    if toppings == "quit":
        active = False
    else:
        print(f"\n I will add {toppings} to your pizza.")
