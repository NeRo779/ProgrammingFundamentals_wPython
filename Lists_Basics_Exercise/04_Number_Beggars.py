cash_str = input().split(", ")
beggars_count = int(input())

cash_int = []

for current_cash in cash_str:
    cash_int.append(int(current_cash))
final_sum = []
starting_sum = 0

while starting_sum < beggars_count:
    current_beggar = 0
    for current_sum in range(starting_sum, len(cash_int), beggars_count):
        current_beggar += cash_int[current_sum]
    final_sum.append(current_beggar)
    starting_sum += 1
print(final_sum)
