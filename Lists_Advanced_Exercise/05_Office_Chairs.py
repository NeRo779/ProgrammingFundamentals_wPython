def current_room(number_of_rooms):
    free_chairs = 0

    for number_of_rooms in range(1, number_of_rooms + 1):
        current_free_chairs, visitors = input().split()
        difference = len(current_free_chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_rooms}")
        free_chairs += difference
    return free_chairs

total_rooms = int(input())
total_free_chairs = current_room(total_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

