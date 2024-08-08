event = input()
coffee = 0

while event != 'END':
    if event == 'coding' or event == 'dog' or event == 'cat' or event == 'movie':
        coffee += 1
    elif event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        coffee += 2

    event = input()

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)

