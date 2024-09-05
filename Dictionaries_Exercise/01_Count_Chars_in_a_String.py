characters = [character for character in input() if character != " "]
letters = {}
for char in characters:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")

