import math

inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(int(line))

print(inputlines)

sum = 0

for line in inputlines:
    sum += (math.floor(line / 3) - 2)

print(sum)
