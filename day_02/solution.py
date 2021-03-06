import os
from typing import List, Tuple


def parse_passwords(file_path: str) -> List[Tuple]:
    password_data = []
    with open(file_path) as f:
        for line in f:
            split_line = line.split()
            numbers = split_line[0].split('-')
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            letter = split_line[1][0]
            password = split_line[2]
            password_data.append((num1, num2, letter, password))
    return password_data


def first_star(password_data: List[Tuple]) -> int:
    valid_count = 0
    for num1, num2, letter, password in password_data:
        count = password.count(letter)
        if num1 <= count <= num2:
            valid_count += 1
    return valid_count


def second_star(password_data: List[Tuple]) -> int:
    valid_count = 0
    for num1, num2, letter, password in password_data:
        is_position_1 = password[num1 - 1] == letter
        is_position_2 = password[num2 - 1] == letter

        if is_position_1 + is_position_2 == 1:
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse_passwords(input_file_path)
    print(first_star(input_data))  # 580
    print(second_star(input_data))  # 611
