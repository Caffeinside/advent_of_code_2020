import os
from typing import List


def parse_xmas_numbers(file_path: str) -> List[int]:
    f = open(file_path, 'r')
    return [int(line.replace('\n', '')) for line in f.readlines()]


def find_first_number_not_sum_of_two_of_previous_25_numbers(xmas_numbers: List[int]) -> int:
    for i in range(0, len(xmas_numbers[25:])):
        previous_numbers = xmas_numbers[i:25 + i]
        current_number = xmas_numbers[25:][i]
        sum_found_in_previous_numbers = False

        for x in range(0, len(previous_numbers)):
            for y in range(x + 1, len(previous_numbers)):
                if previous_numbers[x] + previous_numbers[y] == current_number:
                    sum_found_in_previous_numbers = True
                    break

        if not sum_found_in_previous_numbers:
            return current_number


def find_encryption_weakness(xmas_numbers: List[int]) -> int:
    sum_to_find = find_first_number_not_sum_of_two_of_previous_25_numbers(xmas_numbers)

    for i in range(0, len(xmas_numbers)):
        current_sum = 0
        for j in range(i, len(xmas_numbers)):
            current_sum += xmas_numbers[j]
            if current_sum == sum_to_find:
                result_list = [xmas_numbers[x] for x in range(i, j + 1)]
                return min(result_list) + max(result_list)
            if current_sum > sum_to_find:
                break


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    xmas_numbers_data = parse_xmas_numbers(input_file_path)
    print('Solution 1: ', find_first_number_not_sum_of_two_of_previous_25_numbers(xmas_numbers_data))  # 29221323
    print('Solution 2: ', find_encryption_weakness(xmas_numbers_data))  # 4389369
