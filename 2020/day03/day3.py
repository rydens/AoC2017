# day 3
inputlines = [line.strip('\n') for line in open('input.txt', 'r')]

trees = 0
xComponent = 3

# For debugging
def highlightThing(string, i):
    return string[:i] + '\033[43m' + string[i] + '\033[49m' + string[i+1:]

for i in range(1, len(inputlines)):
    #print(xComponent, '\t', highlightThing(inputlines[i], xComponent))
    if (inputlines[i][xComponent] == '#'):
        trees += 1
    
    xComponent += 3
    if xComponent >= len(inputlines[0]):
        xComponent %= 31

print(trees)