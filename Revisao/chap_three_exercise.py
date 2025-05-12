# 3-1: Names

# Store the names of a few of your friends in a
# list called names. Print each person's name by
# accessing each element in the list, one at a time.

names = ["cristina", "magdalena", "denis"]
print(names[0])
print(names[1])
print(names[2])

print("-----------------------\n")

# 3-2: Greetings
# Start with the list you used in Exercise 3-1,
# but instead of just printing each person's name,
# print a message to them. The text of each message
# should be the same, but each message should be
# personalized with the person's name.

names = ["cristina", "magdalena", "denis"]

print(f"Hello {names[0].title()}! Nice to see you!")
print(f"Hello {names[1].title()}! Nice to see you!")
print(f"Hello {names[2].title()}! Nice to see you!")

print("-----------------------\n")
# 3-4: Guest List
# If you could invite anyone, living or deceased,
# to dinner, who would you invite? Make a list that
# includes at least three people you'd like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

guests = ["Alan", "Merryl", "Ken"]

for guest in guests:
    print(f"Hello {guest}. Please come to dinner!")


print("-----------------------\n")
# 3-5: Changing Guest List

guests = ["Alan", "Merryl", "Ken"]

print(f"Hello {guests[0]}. Please come to dinner!")
print(f"Hello {guests[1]}. Please come to dinner!")
print(f"Hello {guests[2]}. Please come to dinner!\n")

print(f"Sorry! {guests[2]} cant' come to dinner.\n")

del guests[2]
guests.insert(2, "Emma")

print(f"Hello {guests[2]}. Please come to dinner!")
