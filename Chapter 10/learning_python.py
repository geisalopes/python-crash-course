from pathlib import Path

file_path = Path("Chapter 10/learning_python.txt")

with file_path.open() as file:
    contents = file.read()

for line in contents.splitlines():
    modified_line = line.replace("Python", "C")
    print(modified_line)
