# had to have help on this one:
#  https://www.youtube.com/watch?v=clRDvO3H9fU

CARD_MAP = {
    "T": "A",
    "J": ".",
    "Q": "C",
    "K": "D",
    "A": "E",
}

inputs = open("day7_q1.data").read().split("\n")


def score(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def replacements(hand):
    if hand == "":
        return [""]
    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def classify_hand(hand):
    return max(map(score, replacements(hand)))

def hand_values(hand):
    return classify_hand(hand), [CARD_MAP.get(card, card) for card in hand]


plays = []
for line in inputs:
    hand_data, bid = line.split()
    plays.append((hand_data, int(bid)))

plays.sort(key=lambda play: hand_values(play[0]))

total = 0
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)
