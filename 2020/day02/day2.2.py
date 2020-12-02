# day 2, part 2
inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(line)

def NOR(in1, in2):
    if (in1 or in2) and (in1 != in2):
        return True
    return False

validPasswords = 0

for pw in inputlines:
    pwItem = pw.split(' ')
    pos1 = int(pwItem[0].split('-')[0]) - 1
    pos2 = int(pwItem[0].split('-')[1]) - 1
    validPasswords += 1 if NOR(pwItem[2][pos1] == pwItem[1][0], pwItem[2][pos2] == pwItem[1][0]) else 0

print(validPasswords)