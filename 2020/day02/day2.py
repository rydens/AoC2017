# day 2
inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(line)

validPasswords = 0

for pw in inputlines:
    pwItem = pw.split(' ')
    lower = int(pwItem[0].split('-')[0])
    upper = int(pwItem[0].split('-')[1])
    validPasswords += 1 if (pwItem[2].count(pwItem[1][0]) >= lower and pwItem[2].count(pwItem[1][0]) <= upper) else 0

print(validPasswords)