REPLACEMENTS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_first(line):
    org_line = line
    pointer = 0
    while pointer <= len(line):
        if line[pointer].isdigit():
            return line[pointer]
        else:
            for rep in REPLACEMENTS.keys():
                if line.startswith(rep):
                    return REPLACEMENTS[rep]
            else:
                pointer += 1


def find_last(line):
    org_line = line
    pointer = -1
    while abs(pointer) <= len(line):
        if line[pointer].isdigit():
            return line[pointer]
        else:
            for rep in REPLACEMENTS.keys():
                temp_line = org_line[pointer::]
                if temp_line.startswith(rep):
                    return REPLACEMENTS[rep]
            else:
                pointer -= 1


def process_data_for_question1(data):
    total = 0
    for line in data:
        line = line.strip("\n")
        digits = [val for val in line if val.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


def process_data_for_question2(data):
    total = 0
    for line in data:
        line = line.strip("\n")
        first = find_first(line)
        last = find_last(line)
        total += int(first + last)
    return total


def process_data():
    with open("day1_q1.data", "r") as file_in:
        data = file_in.readlines()

    total_for_question1 = process_data_for_question1(data)
    print(f"Day 1 question 1 total: {total_for_question1}")

    total_for_question2 = process_data_for_question2(data)
    print(f"Day 1 question 2 total: {total_for_question2}")

process_data()
