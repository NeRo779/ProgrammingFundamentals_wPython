courses = int(input())

capacity = 255
added_water = 0

for pour in range(courses):
    liters = int(input())
    if capacity - liters < 0:
        print('Insufficient capacity!')
        continue
    capacity -= liters
    added_water += liters

print(added_water)

