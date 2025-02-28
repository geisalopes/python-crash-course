from pathlib import Path

path = Path("Chapter 10/guest_book.txt")

prompt = "\nHi, what's your name?"
prompt += "\nEnter 'quit' if you are the last guest."

guest_names = []
while True:
    name = input(prompt)
    if name == "quit":
        break

    print(f"Thanks {name}, we'll add you to the guest book.")

# Build a string where "\n" is added after each name.
file_string = ""
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)
