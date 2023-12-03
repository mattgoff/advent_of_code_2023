from collections import deque


def get_data():
    with open("day3_q1.data", "r") as infile:
        data = infile.readlines()

    data = [list(line.strip("\n")) for line in data]
    return data


def part1(board_data):
    total_valid = 0
    for line_idx, line in enumerate(board_data):
        col_pointer = 0
        while col_pointer < len(line):
            if col_pointer == 114:
                print()
            tracker = []
            current_pointer = col_pointer
            while current_pointer < len(line) and line[current_pointer].isdigit():
                tracker.append((line_idx, current_pointer, line[current_pointer]))
                current_pointer += 1
            if col_pointer == current_pointer:
                col_pointer += 1
            else:
                col_pointer += (current_pointer - col_pointer)
                if tracker:
                    total_valid += search_for_count(tracker, board_data)
    return total_valid


def search_for_count(datapoint, board_data):
    value = int(str.join("", [x[2] for x in datapoint]))

    for dp in datapoint:
        row, column, val = dp

        search_up = row - 1, column
        search_right = row, column + 1
        search_down = row + 1, column
        search_left = row, column - 1
        search_diag_up_right = row - 1, column + 1
        search_diag_up_left = row - 1, column - 1
        search_diag_down_right = row + 1, column + 1
        search_diag_down_left = row + 1, column - 1
        scans = [search_up, search_right, search_down, search_left, search_diag_up_right, search_diag_up_left, search_diag_down_right, search_diag_down_left]

        for scan in scans:
            row, col = scan
            if 0 < row < len(board_data) and 0 < col < len(board_data[0]):
                board_val = board_data[row][col] or None

                if board_val and board_val != "." and not board_val.isdigit():
                    return value

    return 0


def part2(board_data):
    total = 0
    for row_idx, row in enumerate(board_data):

        for col_index, char in enumerate(row):
            if char == "*":
                row_minus_one = board_data[row_idx - 1] if row_idx - 1 >= 0 else ['.'] * len(row)
                row_plus_one = board_data[row_idx + 1] if row_idx + 1 < len(board_data) else ['.'] * len(row)
                total += search_2(row_minus_one, row, row_plus_one, col_index)
    return total

def search_2(row_minus_one, row, row_plus_one, asterisk_idx):
    is_up = False
    is_down = False

    column = asterisk_idx
    values = []

    if row_minus_one[column].isdigit():
        # number is above look left and right of that index in row_minus_one
        is_up = True
        values.append(scan_left_and_right_from_idx(row_minus_one, column))

    if row_plus_one[column].isdigit():
        # number is below look left and right of that index in row_minus_one
        is_down = True
        values.append(scan_left_and_right_from_idx(row_plus_one, column))

    if row[column + 1].isdigit():
        # number is right, read right till no more digits
        values.append(scan_right_from_idx(row, column + 1))

    if row[column - 1].isdigit():
        # number is left, read left till no more digit
        values.append(scan_left_from_idx(row, column - 1))

    if row_plus_one[column + 1].isdigit() and not is_down:
        # number is down and right read till no more
        values.append(scan_right_from_idx(row_plus_one, column + 1))

    if row_plus_one[column - 1].isdigit() and not is_down:
        # number is down and left, read till no more
        values.append(scan_left_from_idx(row_plus_one, column - 1))

    if row_minus_one[column + 1].isdigit() and not is_up:
        # number is up and right, read till ...
        values.append(scan_right_from_idx(row_minus_one, column + 1))

    if row_minus_one[column - 1].isdigit() and not is_up:
        # number is up and left, read...
        values.append(scan_left_from_idx(row_minus_one, column - 1))

    if len(values) == 2:
        return values[0] * values[1]
    else:
        return 0


def scan_left_from_idx(row, idx):
    value = deque()
    while idx >= 0 and row[idx].isdigit():
        value.appendleft(row[idx])
        idx -= 1
    return int(str.join("", value))


def scan_right_from_idx(row, idx):
    value = []
    while idx < len(row) and row[idx].isdigit():
        value.append(row[idx])
        idx += 1
    return int(str.join("", value))


def scan_left_and_right_from_idx(row, idx):
    value = deque()
    left_idx = idx
    right_idx = idx + 1
    while left_idx >= 0 and row[left_idx].isdigit():
        value.appendleft(row[left_idx])
        left_idx -= 1
    while right_idx < len(row) and row[right_idx].isdigit():
        value.append(row[right_idx])
        right_idx += 1

    return int(str.join("", value))


data = get_data()
print(part1(data))
print(part2(data))

