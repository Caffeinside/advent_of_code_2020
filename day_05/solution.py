import os
from typing import List


def parse_seats(file_path: str) -> List[str]:
    f = open(file_path, 'r')
    return [line.replace('\n', '') for line in f.readlines()]


def find_max_seat_id(seats) -> int:
    return max(compute_seat_id(seat) for seat in seats)


def find_missing_seat_id(seats) -> int:
    sorted_seat_ids = sorted(compute_seat_id(seat) for seat in seats)
    for i in range(len(sorted_seat_ids)):
        if sorted_seat_ids[i + 1] - sorted_seat_ids[i] == 2:
            return sorted_seat_ids[i] + 1


def compute_seat_id(seat) -> int:
    return find_row(seat) * 8 + find_column(seat)


def find_row(seat: str) -> int:
    row = seat[:7]
    row_binary = row.replace('F', '0').replace('B', '1')
    return int(row_binary, base=2)


def find_column(seat: str) -> int:
    column = seat[7:]
    column_binary = column.replace('R', '1').replace('L', '0')
    return int(column_binary, base=2)


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    seats_data = parse_seats(input_file_path)
    print('Solution 1: ', find_max_seat_id(seats_data))
    print('Solution 2: ', find_missing_seat_id(seats_data))
