line = input().split(" ")
product_price = {}
product_quantity = {}


while "buy" not in line:
    product = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if product not in product_quantity.keys():
        product_quantity[product] = 0
        product_price[product] = 0.00
    product_price[product] = price
    product_quantity[product] += quantity
    line = input().split(" ")

    if "buy" in line:
        break

for key, value in product_quantity.items():
    price = value * product_price[key]
    print(f"{key} -> {price:.2f}")

