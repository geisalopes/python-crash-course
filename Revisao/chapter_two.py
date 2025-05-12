print("2.1----------------------------------\n")
msg = "I love learning to use Python"
print(msg)

print("\n2.2----------------------------------\n")

msg = "I love learning Python"
print(msg)

msg = "It's really satisying!"
print(msg)

print("\n2.3----------------------------------\n")

name = "geisa"
msg = f"Hello {name.title()}, would you like to learn some Python today?"
print(msg)


print("\n2.4----------------------------------\n")

name = "geisa"
print(name.lower())
print(name.upper())
print(name.title())

print("\n2.5----------------------------------\n")

print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')

print("\n2.6----------------------------------\n")

famous_person = "Albert Eisntein"
message = "'A person who never made a mistake, never tried anything new.'"

print(f"{famous_person} once said:{message}")

print("\n2.7----------------------------------\n")
name = "\tGeisa Lopes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

print("\n2.8----------------------------------\n")

filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")
print(simple_filename)

print("\n2.9----------------------------------\n")
fav_num = 14
msg = f"My favorite number is {fav_num}."
print(msg)
