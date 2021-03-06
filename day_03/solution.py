import os
from typing import List


def parse_forest_map(file_path: str) -> List[str]:
    f = open(file_path, 'r')
    return [line.replace('\n', '') for line in f.readlines()]


def count_trees(forest_map: List[str], horizontal_step: int, vertical_step: int) -> int:
    tree_count = 0
    horizontal_position = 0
    vertical_position = 0
    while vertical_position < len(forest_map) - 1:
        horizontal_position = (horizontal_position + horizontal_step) % len(forest_map[0])
        vertical_position += vertical_step
        if forest_map[vertical_position][horizontal_position] == '#':
            tree_count += 1
    return tree_count


def first_star(forest_map: List[str]) -> int:
    return count_trees(forest_map, 3, 1)


def second_star(forest_map: List[str]) -> int:
    result_1_1 = count_trees(forest_map, 1, 1)
    result_3_1 = count_trees(forest_map, 3, 1)
    result_5_1 = count_trees(forest_map, 5, 1)
    result_7_1 = count_trees(forest_map, 7, 1)
    result_1_2 = count_trees(forest_map, 1, 2)

    return result_1_1 * result_3_1 * result_5_1 * result_7_1 * result_1_2


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse_forest_map(input_file_path)
    print(first_star(input_data))  # 200
    print(second_star(input_data))  # 3737923200
