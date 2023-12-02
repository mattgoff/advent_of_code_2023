from operator import mul
from functools import reduce


COLOR_LIMITS = [12, 13, 14]


def collect_data():
    with open("day2_q1.data", "r") as infile:
        data = infile.readlines()
    return data


def get_color(dice):
    if "red" in dice:
        return 0
    elif "green" in dice:
        return 1
    else:
        return 2


def parse_input_data(data_in):
    totals = {}
    for line in data_in:
        game, results = line.split(":")
        game_number = int(game.split(" ")[1])
        sets = results.strip("\n").split(";")
        totals[game_number] = {set_number: [0, 0, 0] for set_number, group in enumerate(sets)}

        for set_number, group in enumerate(sets):
            temp = group.split(",")
            for dice in temp:
                color = get_color(dice)
                totals[game_number][set_number][color] += int(dice.strip().split()[0])
    return totals


def game_maxes(data_in):
    # highest_counts = {}
    # for game in data_in:
    #     scores = zip(*data_in[game].values())
    #     highest_counts[game] = list(map(max, scores))
    # return highest_counts
    return {game: list(map(max, zip(*data_in[game].values()))) for game in data_in}


def find_valid_games(data_in):
    # valid_sum = 0
    # for key, colors in data_in.items():
    #     if colors[0] <= 12 and colors[1] <= 13 and colors[2] <= 14:
    #         valid_sum += key
    # return valid_sum

    return sum(key for key, colors in data_in.items() if colors[0] <= 12 and colors[1] <= 13 and colors[2] <= 14)


def find_power(data_in):
    # total_sum = 0
    # for key, colors in data_in.items():
    #     total_sum += reduce(operator.mul, colors)
    # return total_sum
    return sum(reduce(mul, colors) for colors in data_in.values())


def question_1(data):
    games_scores = parse_input_data(data)
    maxes = game_maxes(games_scores)
    print(f"Question_1: {find_valid_games(maxes)}")


def question_2(data):
    games_scores = parse_input_data(data)
    maxes = game_maxes(games_scores)
    print(f"Question_2 {find_power(maxes)}")


print("Expected results:\n\tQuestion_1: 2505\n\tQuestion_2 70265\nActual:")
data = collect_data()
question_1(data)
question_2(data)


