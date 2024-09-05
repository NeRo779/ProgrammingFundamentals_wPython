total_resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())

    if current_resource not in total_resources.keys():
        total_resources[current_resource] = 0
    total_resources[current_resource] += current_quantity

for resource, quantity in total_resources.items():
    print(f"{resource} -> {quantity}")

