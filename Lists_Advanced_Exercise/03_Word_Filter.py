fruits = input().split()
even_names = [fruit for fruit in fruits if len(fruit) % 2 == 0]
print("\n".join(even_names))

