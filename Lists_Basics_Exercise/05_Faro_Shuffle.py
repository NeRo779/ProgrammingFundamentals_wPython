deck = input().split()
shuffles_count = int(input())

for shuffles in range(shuffles_count):
    middle_deck = len(deck) // 2
    left_deck = deck[0:middle_deck]
    right_deck = deck[middle_deck:]
    deck_after_shuffle = []
    for card_index in range(len(left_deck)):
        deck_after_shuffle.append(left_deck[card_index])
        deck_after_shuffle.append(right_deck[card_index])
        deck = deck_after_shuffle

print(deck_after_shuffle)
