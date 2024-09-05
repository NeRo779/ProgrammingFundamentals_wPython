country = input().split(", ")
capital = input().split(", ")

connected = {country[index]: capital[index] for index in range(len(country))}   #DICT Comprehension Method
connected = dict(zip(country, capital))   #ZIP Method

for country, capital in connected.items():
    print(f"{country} -> {capital}")

