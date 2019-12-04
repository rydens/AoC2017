# aPpArEnTlY Python has a "recursion limit" to prevent stack overflows; and THEN macOS has a "stack guard,"
# so even when you bypass Python's limit, things still don't get fun
steps = open('input.txt', 'r')
wire1 = steps.readline().strip().split(',')
wire2 = steps.readline().strip().split(',')

intersects = open('intersects.txt', 'r')
icoords = []
for line in intersects:
    icoords.append(line.strip())

def moveStep(finalx, finaly, directions):
    curx = 0
    cury = 0
    steps = 0
    while True:
        if curx == finalx and cury == finaly:
            break
#        print(f'{finalx}\n{finaly}\n{directions}\n{curx}\n{cury}\n') 
        if directions[0][0] == 'U':
            pop = directions.pop(0)
            if int(pop[1:]) > 1:
                directions.insert(0, pop[0] + str(int(pop[1:])-1))
            cury += 1
        elif directions[0][0] == 'D':
            pop = directions.pop(0)
            if int(pop[1:]) > 1:
                directions.insert(0, pop[0] + str(int(pop[1:])-1))
            cury -= 1
        elif directions[0][0] == 'L':
            pop = directions.pop(0)
            if int(pop[1:]) > 1:
                directions.insert(0, pop[0] + str(int(pop[1:])-1))
            curx -= 1
        elif directions[0][0] == 'R':
            pop = directions.pop(0)
            if int(pop[1:]) > 1:
                directions.insert(0, pop[0] + str(int(pop[1:])-1))
            curx += 1
        steps += 1
    return steps

totalsteps = []
for isect in icoords:
#    print(isect)
    totalsteps.append(moveStep(int(isect.split(',')[0]), int(isect.split(',')[1]), wire1.copy()) + moveStep(int(isect.split(',')[0]), int(isect.split(',')[1]), wire2.copy()))

lower = totalsteps[0]
for i in totalsteps:
    if i < lower:
        lower = i
print(lower)
