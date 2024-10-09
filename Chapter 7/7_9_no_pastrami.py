# Make a list called sandwich_orders and fill it with the names of various sandwiches
# and then make a empty list called finished_sandwiches.
# Make sure the 'pastrami sandwich' are listed at least three times.
sandwich_orders = [
    "tunah",
    "pastrami",
    "vishvish",
    "chickericki",
    "pastrami",
    "salamini",
    "cheesy",
    "soyballs",
    "pastrami",
]
finished_sandwiches = []

# Add a code near the beggining of your programm to print a message saying the deli has run out of pastrami.
print("Sorry, the deli has run out of Pastrami.\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Loop through the list of sandwich orders and print a message for eache order.
# As each sandwich is made, move it to the list of finished sandwiches.
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

# After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
