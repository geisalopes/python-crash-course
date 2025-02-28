from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data."

path = Path("Chapter 10/programming.txt")
path.write_text(contents)
