# day 3, part 2
inputlines = [line.strip('\n') for line in open('input.txt', 'r')]

# For debugging
def highlightThing(string, i):
    return string[:i] + '\033[43m' + string[i] + '\033[49m' + string[i+1:]

def tryRoute(xCom, yCom):
    trees = 0
    xComponent = xCom

    for i in range(yCom, len(inputlines), yCom):
        #print(i, xComponent, '\t', highlightThing(inputlines[i], xComponent))
        if (inputlines[i][xComponent] == '#'):
            trees += 1
        
        xComponent += xCom
        if xComponent >= len(inputlines[0]):
            xComponent %= len(inputlines[0]) 

    return trees

# part 1
print(len(inputlines[-2]), len(inputlines[-1]))
print(tryRoute(3,1))

# part 2
print(tryRoute(1,1)*tryRoute(3,1)*tryRoute(5,1)*tryRoute(7,1)*tryRoute(1,2))