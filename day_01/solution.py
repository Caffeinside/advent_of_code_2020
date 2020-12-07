import os
from typing import List


def parse_expenses(file_path: str) -> List[int]:
    f = open(file_path, 'r')
    return [int(line) for line in f.readlines()]


def first_star(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        for j in range(i + 1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]


def second_star(expenses: List[int]) -> int:
    for i in range(len(expenses)):
        for j in range(i + 1, len(expenses)):
            for k in range(j + 1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i] * expenses[j] * expenses[k]


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    expenses_list = parse_expenses(input_file_path)
    print(first_star(expenses_list))  # 988771
    print(second_star(expenses_list))  # 171933104
