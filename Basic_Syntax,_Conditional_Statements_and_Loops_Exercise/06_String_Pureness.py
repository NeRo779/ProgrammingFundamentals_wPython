string_count = int(input())

for current_string in range(string_count):
    string = input()
    if ',' in string or '.' in string or '_' in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')

