number_of_orders = int(input())
coffee_price = 0
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

# 1st way
    # if not 0.01 <= price_per_capsule <= 100.00:
    #     continue
    # days = int(input())
    # if not 1 <= days <= 31:
    #     continue
    # capsules_per_day = int(input())
    # if not 1 <= capsules_per_day <= 2000:
    #     continue

# 2nd way
    if not 0.01 <= price_per_capsule <= 100.00 \
            or not 1 <= days <= 31 \
            or not 1 <= capsules_per_day <= 2000:
        continue

    coffee_price = price_per_capsule * days * capsules_per_day
    print(f'The price for the coffee is: ${coffee_price:.2f}')
    total_price += coffee_price

print(f'Total: ${total_price:.2f}')
