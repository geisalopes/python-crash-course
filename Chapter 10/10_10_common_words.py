from pathlib import Path

path = Path("alice.txt")
contents = path.read_text(encoding="utf-8")

lower_contents = contents.lower()

word_count = lower_contents.count("rabbit")

print(f"The word 'rabbit' shows {word_count} times in the book.")
