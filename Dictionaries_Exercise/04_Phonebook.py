phonebook = {}

while True:
    info = input()
    if "-" not in info:
        break
    name, phone_number = info.split("-")
    phonebook[name] = phone_number

searches = int(info)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

