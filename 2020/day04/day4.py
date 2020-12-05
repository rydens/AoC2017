# day 4
passports = [line.split() for line in open('input.txt', 'r').read().split('\n\n')]

reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # but not cid

def checkFields(passport):
    fields = [field.split(':')[0] for field in passport]
    for reqField in reqFields:
        if reqField not in fields:
            return False

    return True


validPassports = 0

for passport in passports:
    validPassports += 1 if checkFields(passport) else 0

print(validPassports)
        