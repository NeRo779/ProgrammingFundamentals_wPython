strings = input().split(" ")
result = ""

for string in strings:
    string_length = len(string)
    result += string_length * string
print(result)
