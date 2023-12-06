from concurrent.futures import ThreadPoolExecutor


def get_data():
    with open("day5_q1.data", "r") as infile:
        data = infile.readlines()
    return data


def parse_data(data):
    pointer = 0
    key, values = data[pointer].split(":")
    seed_map = {
        key: list(map(int, values.split()))
    }
    pointer += 1

    while pointer < len(data):
        line = data[pointer].strip()
        if line:
            values = []
            if line[0].isalpha():
                key = line.split(" ")[0]
            pointer += 1
            while pointer < len(data) and data[pointer][0].isdigit():
                dest, src, rg = data[pointer].split(" ")
                destination = [int(dest), int(dest) + int(rg.strip()) - 1]
                source = [int(src), int(src) + int(rg.strip()) - 1]
                values.append([destination, source])
                pointer += 1
            seed_map[key] = values
        else:
            pointer += 1

    return seed_map


def part1(data):
    seeds = data['seeds']
    datapoints = [
        'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
        'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
        'humidity-to-location'
    ]

    locations = []
    for seed in seeds:
        print(f"{seed}")
        print(f"-" * 40)
        current_value = seed
        for dp in datapoints:
            current_value = number_lookup(data, dp, current_value)
            # print(f"{dp=} {seed=} maps to {current_value=}")
        locations.append(current_value)
        print()
    print(f"Location = {min(locations)=} ")

def number_lookup(data, key, value):
    for ranges in data[key]:
        lower, upper = ranges[1]
        is_in_range = lower <= value <= upper
        if is_in_range:
            offset = value - lower
            return ranges[0][0] + offset
    return value

def part2(data):
    seeds = data['seeds']
    datapoints = [
        'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
        'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
        'humidity-to-location'
    ]

    # this couldn't be uglier
    locations = []
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            current_value = seed
            for dp in datapoints:
                current_value = number_lookup(data, dp, current_value)
            locations.append(current_value)
        print(".", end="")
    print(f"\nLocation = {min(locations)=} ")


data = get_data()
data_parsed = parse_data(data)

part1(data_parsed)
part2(data_parsed)
