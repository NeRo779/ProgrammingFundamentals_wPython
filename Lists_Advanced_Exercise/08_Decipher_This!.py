message = input().split(" ")
decipher = []

for word in message:
    ascii_table = [char for char in word if char.isdigit()]
    word_list = [char for char in word if char not in ascii_table]

    first_letter = chr(int("".join(ascii_table)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + ''.join(word_list)
    decipher.append(new_word)

print(" ".join(decipher))

