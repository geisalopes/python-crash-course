from pathlib import Path

file_path = Path("pi_digits.txt")
contents = file_path.read_text()
print(contents)
