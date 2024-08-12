def odd_even_sum(number: str):
    even_sum = 0
    odd_sum = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return even_sum, odd_sum

inp_number = input()
even_digits_sum, odd_digits_sum = odd_even_sum(inp_number)
print(f'Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}')

