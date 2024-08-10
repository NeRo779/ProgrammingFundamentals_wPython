starting_index = int(input())
last_character = int(input())

for index in range(starting_index, last_character + 1):
    print(chr(index), end=' ')

