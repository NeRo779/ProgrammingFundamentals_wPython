def is_perfect(number: int) -> str:
    total_divisors = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            total_divisors += divisor
    if number == total_divisors:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

starting_number = int(input())
print(is_perfect(starting_number))

