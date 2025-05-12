from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
        lines = contents.splitlines()
        print(f"\nContents of {filename}:")
        for line in lines:
            print(f"- {line}")
    except FileNotFoundError:
        print(f"\nSorry, the file {filename} was not found.")
