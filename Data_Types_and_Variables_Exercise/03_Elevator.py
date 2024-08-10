import math
number_of_people = int(input())
capacity_p = int(input())

courses = math.ceil(number_of_people / capacity_p)

print(courses)
