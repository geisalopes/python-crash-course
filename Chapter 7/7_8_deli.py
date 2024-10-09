# Make a list called sandwich_orders and fill it with the names of various sandwiches
# and then make a empty list called finished_sandwiches.
sandwich_orders = ["tunah", "vishvish", "chickericki", "salamini", "cheesy", "soyballs"]
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for eache order.
# As each sandwich is made, move it to the list of finished sandwiches.
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I am working on your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)

# After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
