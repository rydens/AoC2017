import math

inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(int(line))

sum = 0

def getFuel(mass):
    if mass <= 6:
        return 0
    fuel = math.floor(mass / 3) - 2
    return fuel + getFuel(fuel)

for module in inputlines:
    sum += getFuel(module)

print(sum)
