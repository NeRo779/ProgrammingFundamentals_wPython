string_numbers = input().split()
sorted_list = []
for number in string_numbers:
    sorted_list.append(int(number))
result = list(sorted(sorted_list))
print(result)

