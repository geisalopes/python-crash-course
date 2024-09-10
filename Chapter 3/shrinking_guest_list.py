guests = ["alan", "merryl", "emma"]
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

guests[1] = "maggie"

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

print("\nI found a big table!")

guests.insert(0, "anthony")
guests.insert(2, "ellen")
guests.append("ian")

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there is no room at the table")

name = guests.pop()
print("Sorry, " + name.title() + " there is no room at the table")

name = guests.pop()
print("Sorry, " + name.title() + " there is no room at the table")

name = guests.pop()
print("Sorry, " + name.title() + " there is no room at the table")

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

del guests[0]
del guests[0]

print(guests)
