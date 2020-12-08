import os
from typing import List, Tuple


def parse_instructions(file_path: str) -> List[List[str]]:
    f = open(file_path, 'r')
    return [line.replace('\n', '').split() for line in f.readlines()]


def get_accumulator_value_before_second_execution(instructions: List[List[str]]) -> int:
    accumulator, _ = execute_instructions(instructions)
    return accumulator


def get_accumulator_value_after_termination(instructions: List[List[str]]) -> int:
    indexes_to_invert = [i for i, value in enumerate(instructions) if (value[0] == 'nop') or (value[0] == 'jmp')]
    for index_to_invert in indexes_to_invert:
        accumulator, program_terminated = execute_instructions(instructions, index_to_invert)
        if program_terminated:
            return accumulator


def execute_instructions(instructions: List[List[str]], index_to_invert: int = None) -> Tuple[int, bool]:
    i = 0
    is_executed = []
    accumulator = 0
    program_terminated = False
    while i not in is_executed:
        if i == len(instructions):
            program_terminated = True
            break
        if instructions[i][0] == 'nop' and i == index_to_invert:
            is_executed.append(i)
            i += int(instructions[i][1])
        elif instructions[i][0] == 'jmp' and i == index_to_invert:
            is_executed.append(i)
            i += 1
        elif instructions[i][0] == 'nop':
            is_executed.append(i)
            i += 1
        elif instructions[i][0] == 'acc':
            accumulator += int(instructions[i][1])
            is_executed.append(i)
            i += 1
        elif instructions[i][0] == 'jmp':
            is_executed.append(i)
            i += int(instructions[i][1])

    return accumulator, program_terminated


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    instructions_data = parse_instructions(input_file_path)
    print('Solution 1: ', get_accumulator_value_before_second_execution(instructions_data))  # 1818
    print('Solution 2: ', get_accumulator_value_after_termination(instructions_data))  # 631
