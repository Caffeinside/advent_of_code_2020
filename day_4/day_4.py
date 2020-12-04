import re
from typing import List

MANDATORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_passports(filename: str) -> List[dict]:
    passports = []
    individual_passport = {}
    with open(filename) as f:
        for line in f:
            if line[:-1] == '':
                passports.append(individual_passport)
                individual_passport = {}
            else:
                info_on_line = line[:-1].split()
                for info in info_on_line:
                    key_value = info.split(':')
                    individual_passport[key_value[0]] = key_value[1]
    passports.append(individual_passport)
    return passports


def first_star(passports: List[dict]) -> int:
    valid_count = 0
    for passport in passports:
        if all(item in passport.keys() for item in MANDATORY_FIELDS):
            valid_count += 1
    return valid_count


def second_star(passports: List[dict]) -> int:
    valid_count = 0
    for passport in passports:
        if all(item in passport.keys() for item in MANDATORY_FIELDS):
            is_valid = check_validation_rules(passport)
            if is_valid:
                valid_count += 1
    return valid_count


def check_validation_rules(passport: dict) -> bool:
    valid_byr = 1920 <= int(passport['byr']) <= 2002
    valid_iyr = 2010 <= int(passport['iyr']) <= 2020
    valid_eyr = 2020 <= int(passport['eyr']) <= 2030

    ght_suffix = passport['hgt'][-2:]
    if ght_suffix == 'cm':
        valid_hgt = 150 <= int(passport['hgt'][:-2]) <= 193
    elif ght_suffix == 'in':
        valid_hgt = 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        valid_hgt = False

    valid_hcl = re.fullmatch('#[a-f0-9]{6}', passport['hcl'])
    valid_ecl = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_pid = re.fullmatch('[0-9]{9}', passport['pid'])

    return valid_byr and valid_ecl and valid_eyr and valid_hcl and valid_hgt and valid_iyr and valid_pid


if __name__ == '__main__':
    input_data = parse_passports('./day_4/input.txt')
    print(first_star(input_data))
    print(second_star(input_data))
