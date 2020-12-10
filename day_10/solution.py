import os
from typing import List, Dict, Tuple


def parse_adapters_joltage(file_path: str) -> List[int]:
    f = open(file_path, 'r')
    return [int(line.replace('\n', '')) for line in f.readlines()]


def get_distribution_of_joltage_differences(adapters_joltage: List[int]) -> int:
    sorted_adapters_joltage = sort_and_complete_adapters_joltage(adapters_joltage)

    differences = [a - b for a, b in zip(sorted_adapters_joltage[1:], sorted_adapters_joltage[:-1])]
    count_1_jolt_differences = sum([difference == 1 for difference in differences])
    count_3_jolt_differences = sum([difference == 3 for difference in differences])
    return count_1_jolt_differences * count_3_jolt_differences


def sort_and_complete_adapters_joltage(adapters_joltage: List[int]) -> List[int]:
    sorted_adapters_joltage = sorted(adapters_joltage)
    return [0] + sorted_adapters_joltage + [sorted_adapters_joltage[-1] + 3]


def get_total_number_of_distinct_arrangements(adapters_joltage: List[int]) -> int:
    sorted_adapters_joltage = sort_and_complete_adapters_joltage(adapters_joltage)
    return count_combinations(sorted_adapters_joltage)


def count_combinations(sorted_adapters_joltage: List[int], combinations_cache: Dict[Tuple[int], int] = None) -> int:
    if combinations_cache is None:
        combinations_cache = {}

    cache_key = tuple(sorted_adapters_joltage)
    if len(sorted_adapters_joltage) == 1:
        combinations_count = 1
    elif cache_key in combinations_cache:
        combinations_count = combinations_cache[cache_key]
    else:
        combinations_count = sum(
            [count_combinations(sorted_adapters_joltage[next_valid_index:], combinations_cache) for next_valid_index in
             get_next_valid_indices(sorted_adapters_joltage)])
    combinations_cache[cache_key] = combinations_count
    return combinations_count


def get_next_valid_indices(sorted_adapters_joltage: List[int]) -> List[int]:
    next_valid_indices = []
    for i in range(1, min(4, len(sorted_adapters_joltage))):
        if sorted_adapters_joltage[i] - sorted_adapters_joltage[0] <= 3:
            next_valid_indices.append(i)
    return next_valid_indices


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    adapters_joltage_data = parse_adapters_joltage(input_file_path)
    print('Solution 1: ', get_distribution_of_joltage_differences(adapters_joltage_data))  # 2775
    print('Solution 2: ', get_total_number_of_distinct_arrangements(adapters_joltage_data))  # 518344341716992
