# day 4, part 2
import re

passports = [line.split() for line in open('input.txt', 'r').read().split('\n\n')]

reqFields = {
    'byr': '^19[2-9]\d|200[0-2]$',
    'iyr': '^20(1\d|20)$',
    'eyr': '^20(2\d|30)$',
    'hgt': '^1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in$',
    'hcl': '^#[0-9a-f]{6}$',
    'ecl': '^amb|blu|brn|gry|grn|hzl|oth$',
    'pid': '^\d{9}$',
    'cid': ''   # cid doesn't matter
}

def checkFields(passport):
    for reqField in list(reqFields.keys())[:-1]:
        if reqField not in [entry.split(':')[0] for entry in passport]:
            return False

    for entry in [field.split(':') for field in passport]:
        if not re.match(reqFields[entry[0]], entry[1]):
            return False

    return True


validPassports = 0

for passport in passports:
    validPassports += 1 if checkFields(passport) else 0

print(validPassports)
        