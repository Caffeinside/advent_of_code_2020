import os
from functools import reduce
from typing import List


def parse_answers(file_path: str) -> List[str]:
    f = open(file_path, 'r')
    return [line.replace('\n', '') for line in f.readlines()]


def get_answers_for_each_group(answers: List[str]) -> List[List[str]]:
    groups = []
    group_answer = ''
    for answer in answers:
        if answer == '':
            groups.append(group_answer)
            group_answer = ''
        else:
            group_answer += answer + ' '
    groups.append(group_answer)
    return [group.split() for group in groups]


def get_sum_of_questions_answers_by_anyone_in_all_groups(answers_for_each_group: List[List[str]]) -> int:
    return sum(count_questions_answered_by_anyone_in_group(group) for group in answers_for_each_group)


def get_sum_of_questions_answers_by_everyone_in_all_groups(answers_for_each_group: List[List[str]]) -> int:
    return sum(count_questions_answered_by_everyone_in_group(group) for group in answers_for_each_group)


def count_questions_answered_by_anyone_in_group(group_answers: List[str]) -> int:
    unique_answers = (set(one_answer) for one_answer in group_answers)
    return len(reduce(lambda x, y: x.union(y), unique_answers))


def count_questions_answered_by_everyone_in_group(group_answers: List[str]) -> int:
    unique_answers = (set(one_answer) for one_answer in group_answers)
    return len(reduce(lambda x, y: x.intersection(y), unique_answers))


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    answers_data = parse_answers(input_file_path)
    answers_by_group = get_answers_for_each_group(answers_data)
    print('Solution 1: ', get_sum_of_questions_answers_by_anyone_in_all_groups(answers_by_group))  # 6809
    print('Solution 2: ', get_sum_of_questions_answers_by_everyone_in_all_groups(answers_by_group))  # 3394
