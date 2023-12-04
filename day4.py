def get_data():
    with open("day4_q1.data", "r") as infile:
        data = infile.readlines()
    return data

def part1(card_data):
    total_score = 0
    for row in card_data:
        winning, mine = row.split(":")[1].strip().split("|")
        winning = [int(num) for num in winning.split(" ") if num.isdigit()]
        mine = [int(num) for num in mine.split(" ") if num.isdigit()]
        matched = [x for x in mine if x in winning]
        if len(matched) > 0:
            total_score += 1 * (2 ** (len(matched) - 1))
    return total_score


def part2(card_data):
    scores = {}
    for idx, row in enumerate(card_data):
        winning, mine = row.split(":")[1].strip().split("|")
        winning = [int(num) for num in winning.split(" ") if num.isdigit()]
        mine = [int(num) for num in mine.split(" ") if num.isdigit()]
        matched = [x for x in mine if x in winning]
        process_2(scores, idx, len(matched))
    return sum(scores.values())


def process_2(scores, idx, matched_count):
    idx += 1
    scores[idx] = scores.get(idx, 0) + 1
    if matched_count > 0:
        for y in range(scores[idx]):
            for i in range(idx + 1, idx + matched_count + 1):
                scores[i] = scores.get(i, 0) + 1



card_data = get_data()
print(f"{part1(card_data)=}")
print(f"{part2(card_data)=}")
