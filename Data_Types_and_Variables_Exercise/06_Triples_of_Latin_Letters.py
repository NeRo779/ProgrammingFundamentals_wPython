integer = int(input())

for first in range(integer):
    for second in range(integer):
        for third in range(integer):
            print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')

