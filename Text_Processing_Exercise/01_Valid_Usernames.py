def username_check(usernames: str):
    return " " not in usernames

def length_check(usernames: str):
    return 3 <= len(usernames) <= 16

def symbols_check(usernames: str):
    for current_username in usernames:
        if not current_username.isalnum():
            if current_username != "_" and current_username != "-":
                return False
    return True

def username_validation(current_username: str):
    first_check = username_check(current_username)
    second_check = length_check(current_username)
    third_check = symbols_check(current_username)
    return first_check and second_check and third_check

username_list = input().split(", ")
for user in username_list:
    if username_validation(user):
        print(user)

