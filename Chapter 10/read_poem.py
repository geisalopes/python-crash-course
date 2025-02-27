from pathlib import Path

file_path = Path("Chapter 10/poem.txt")

with file_path.open() as file:
    contents = file.read()

words = contents.split()
num_words = len(words)

print(f"O numero total de palavras no poema e {num_words}")
