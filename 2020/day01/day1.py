# day 1
inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(int(line))

print(inputlines)

num1 = 0
num2 = 1

while (inputlines[num1] + inputlines[num2]) != 2020:
    num2 += 1
    if num2 == len(inputlines):
        num1 += 1
        num2 = num1 + 1

print(inputlines[num1] * inputlines[num2])