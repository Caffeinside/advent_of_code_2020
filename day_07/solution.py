import os
from typing import List, Dict


def parse_luggage_rules(file_path: str) -> List[str]:
    f = open(file_path, 'r')
    return [line.replace('\n', '').replace(',', '').replace('.', '') for line in f.readlines()]


def create_bags_dict(luggage_rules: List[str]) -> Dict[str, dict]:
    bags_dict = {}
    for rule in luggage_rules:
        rule_as_list = rule.split()
        luggage = rule_as_list[0] + ' ' + rule_as_list[1]

        bags_dict[luggage] = {}
        if 'no' not in rule_as_list:
            content = rule_as_list[4:]
            for index, element in enumerate(content):
                if element == 'bag' or element == 'bags':
                    color = content[index - 2] + ' ' + content[index - 1]
                    count = content[index - 3]
                    bags_dict[luggage][color] = count

    return bags_dict


def count_bags_eventually_containing_shiny_gold(luggage_rules: List[str]) -> int:
    bags_dict = create_bags_dict(luggage_rules)
    tmp_possible_bags = possible_bags = search_bags_containing_bags(bags_dict, ['shiny gold'])

    while tmp_possible_bags:
        tmp_possible_bags = search_bags_containing_bags(bags_dict, tmp_possible_bags)
        possible_bags.extend(tmp_possible_bags)
    return len(set(possible_bags))


def count_individual_bags_required_in_shiny_gold(luggage_rules: List[str]) -> int:
    bags_dict = create_bags_dict(luggage_rules)
    return count_children_bags('shiny gold', bags_dict)


def count_children_bags(parent_color: str, bags_dict: Dict[str, dict]) -> int:
    bags_count = 0
    children_dict = bags_dict[parent_color]
    bags_count += sum(int(count) for color, count in children_dict.items()) + \
                  sum(int(count) * count_children_bags(color, bags_dict) for color, count in children_dict.items())
    return bags_count


def search_bags_containing_bags(bags_dict: dict, colors: List[str]) -> List[str]:
    bags_containing_colors = []
    for color_containing, color_contained_dict in bags_dict.items():
        matching_colors = [color for color in colors if color in color_contained_dict.keys()]
        if matching_colors:
            bags_containing_colors.append(color_containing)
    return bags_containing_colors


if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    luggage_rules_data = parse_luggage_rules(input_file_path)
    print('Solution 1: ', count_bags_eventually_containing_shiny_gold(luggage_rules_data))  # 211
    print('Solution 2: ', count_individual_bags_required_in_shiny_gold(luggage_rules_data))  # 12414
