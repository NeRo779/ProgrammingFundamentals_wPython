def is_palindrome(number: str):
    return number == number [::-1]

number = input().split(", ")

for number in number:
    print(is_palindrome(number))

