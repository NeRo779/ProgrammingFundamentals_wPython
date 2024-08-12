string_numbers = input().split()
digit_numbers = []
for number in string_numbers:
    digit_numbers.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, digit_numbers))
print(result)

