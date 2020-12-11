import os
from typing import List


def parse_seat_layout(file_path: str) -> List[List[str]]:
    f = open(file_path, 'r')
    return [list(line.replace('\n', '')) for line in f.readlines()]


def get_final_occupied_seats_based_on_rules(seat_layout: List[List[str]], rules_function: callable) -> int:
    is_updated = True
    while is_updated:
        updated_seat_layout = get_updated_layout(seat_layout, rules_function)
        is_updated = check_if_updated_layout(seat_layout, updated_seat_layout)
        seat_layout = updated_seat_layout
    return sum([seat_layout[row][col] == '#' for row in range(len(seat_layout)) for col in range(len(seat_layout[0]))])


def get_updated_layout(seat_layout: List[List[str]], rules_function: callable) -> List[List[str]]:
    updated_seat_layout = [[[] for col in range(len(seat_layout[0]))] for row in range(len(seat_layout))]
    for row in range(len(seat_layout)):
        for col in range(len(seat_layout[0])):
            updated_seat_layout[row][col] = rules_function(seat_layout, row, col)
    return updated_seat_layout


def check_if_updated_layout(seat_layout: List[List[str]], updated_seat_layout: List[List[str]]) -> bool:
    is_updated = False
    for row in range(len(seat_layout)):
        for col in range(len(seat_layout[0])):
            if updated_seat_layout[row][col] != seat_layout[row][col]:
                is_updated = True
    return is_updated


def update_seat_based_on_proximity(seat_layout: List[List[str]], row: int, col: int) -> str:
    seat = seat_layout[row][col]
    adjacent_seats = get_adjacent_seats(seat_layout, row, col)
    if seat == 'L' and sum([(seat != '#') for seat in adjacent_seats]) == len(adjacent_seats):
        updated_seat = '#'
    elif seat == '#' and (sum([seat == '#' for seat in adjacent_seats]) >= 4):
        updated_seat = 'L'
    else:
        updated_seat = seat
    return updated_seat


def update_seat_based_on_visibility(seat_layout: List[List[str]], row: int, col: int) -> str:
    seat = seat_layout[row][col]
    visible_seats = get_visible_seats(seat_layout, row, col)
    if seat == 'L' and sum([(seat != '#') for seat in visible_seats]) == len(visible_seats):
        updated_seat = '#'
    elif seat == '#' and (sum([seat == '#' for seat in visible_seats]) >= 5):
        updated_seat = 'L'
    else:
        updated_seat = seat
    return updated_seat


def get_adjacent_seats(seat_layout: List[List[str]], row: int, col: int) -> List[str]:
    adjacent_seats = []
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            boundary_check_row = 0 <= row + row_offset <= len(seat_layout) - 1
            boundary_check_col = 0 <= col + col_offset <= len(seat_layout[0]) - 1
            if (row_offset != 0 or col_offset != 0) and boundary_check_row and boundary_check_col:
                if row_offset != 0 or col_offset != 0:
                    adjacent_seats += seat_layout[row + row_offset][col + col_offset]

    return adjacent_seats


def get_visible_seats(seat_layout: List[List[str]], row: int, col: int) -> List[str]:
    res1 = check_dim_1(seat_layout, row, col)
    res2 = check_dim_2(seat_layout, row, col)
    res3 = check_dim_3(seat_layout, row, col)
    res4 = check_dim_4(seat_layout, row, col)
    res5 = check_dim_5(seat_layout, row, col)
    res6 = check_dim_6(seat_layout, row, col)
    res7 = check_dim_7(seat_layout, row, col)
    res8 = check_dim_8(seat_layout, row, col)

    return [res1, res2, res3, res4, res5, res6, res7, res8]


def check_dim_1(seat_layout, input_row, input_col):
    for row in range(input_row - 1, -1, -1):
        if seat_layout[row][input_col] == '.':
            continue
        else:
            return seat_layout[row][input_col]


def check_dim_5(seat_layout, input_row, input_col):
    for row in range(input_row + 1, len(seat_layout)):
        if seat_layout[row][input_col] == '.':
            continue
        else:
            return seat_layout[row][input_col]


def check_dim_7(seat_layout, input_row, input_col):
    for col in range(input_col - 1, -1, -1):
        if seat_layout[input_row][col] == '.':
            continue
        else:
            return seat_layout[input_row][col]


def check_dim_3(seat_layout, input_row, input_col):
    for col in range(input_col + 1, len(seat_layout[0])):
        if seat_layout[input_row][col] == '.':
            continue
        else:
            return seat_layout[input_row][col]


def check_dim_2(seat_layout, input_row, input_col):
    offset = 1
    while True:
        if input_row - offset == -1 or input_col + offset == len(seat_layout[0]):
            break
        if seat_layout[input_row - offset][input_col + offset] == '.':
            offset += 1
            continue
        else:
            return seat_layout[input_row - offset][input_col + offset]


def check_dim_6(seat_layout, input_row, input_col):
    offset = 1
    while True:
        if input_row + offset == len(seat_layout) or input_col - offset == -1:
            break
        if seat_layout[input_row + offset][input_col - offset] == '.':
            offset += 1
            continue
        else:
            return seat_layout[input_row + offset][input_col - offset]


def check_dim_8(seat_layout, input_row, input_col):
    offset = 1
    while True:
        if input_row - offset == -1 or input_col - offset == -1:
            break
        if seat_layout[input_row - offset][input_col - offset] == '.':
            offset += 1
            continue
        else:
            return seat_layout[input_row - offset][input_col - offset]


def check_dim_4(seat_layout, input_row, input_col):
    offset = 1
    while True:
        if input_row + offset == len(seat_layout) or input_col + offset == len(seat_layout[0]):
            break
        if seat_layout[input_row + offset][input_col + offset] == '.':
            offset += 1
            continue
        else:
            return seat_layout[input_row + offset][input_col + offset]


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    seat_layout_data = parse_seat_layout(input_file_path)
    assert get_final_occupied_seats_based_on_rules(seat_layout_data, update_seat_based_on_proximity) == 2494
    assert get_final_occupied_seats_based_on_rules(seat_layout_data, update_seat_based_on_visibility) == 2306
    # print('Solution 1: ', solution1(seat_layout_data))  # 2494
    # print('Solution 2: ', solution2(seat_layout_data))  # 2306
