import os


def parse_instructions(file_path):
    f = open(file_path, 'r')
    return [line.replace('\n', '').split() for line in f.readlines()]


def func1(instructions):
    accumulator, _ = execute_instructions(instructions)
    return accumulator


def func2(instructions):
    indexes_to_invert = [i for i, value in enumerate(instructions) if (value[0] == 'nop') or (value[0] == 'jmp')]

    for index_to_invert in indexes_to_invert:
        accumulator, problem_solved = execute_instructions(instructions, index_to_invert)
        if problem_solved:
            return accumulator


def execute_instructions(instructions, index_to_invert=None):
    i = 0
    is_executed = []
    accumulator = 0
    problem_solved = False
    while i not in is_executed:
        if i == len(instructions):
            problem_solved = True
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

    return accumulator, problem_solved


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    instructions_data = parse_instructions(input_file_path)
    print('Solution 1: ', func1(instructions_data))  # 1818
    print('Solution 2: ', func2(instructions_data))  # 631
