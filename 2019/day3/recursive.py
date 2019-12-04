# aPpArEnTlY Python has a "recursion limit" to prevent stack overflows; and THEN macOS has a "stack guard,"
# so even when you bypass Python's limit, things still don't get fun
steps = open('testinput.txt', 'r')
wire1 = steps.readline().strip().split(',')
wire2 = steps.readline().strip().split(',')

intersects = open('testintersects.txt', 'r')
icoords = []
for line in intersects:
    icoords.append(line.strip())

def moveStep(finalx, finaly, directions, curx, cury):
#    print(f'{finalx}\n{finaly}\n{directions}\n{curx}\n{cury}\n')
    if len(directions) == 0:
        print('AAAAAAAAAAH')
        exit()
    if curx == finalx and cury == finaly:
        return 0
    if directions[0][0] == 'U':
        pop = directions.pop(0)
        if int(pop[1:]) > 1:
            directions.insert(0, pop[0] + str(int(pop[1:])-1))
        return 1 + moveStep(finalx, finaly, directions, curx, cury + 1)
    elif directions[0][0] == 'D':
        pop = directions.pop(0)
        if int(pop[1:]) > 1:
            directions.insert(0, pop[0] + str(int(pop[1:])-1))
        return 1 + moveStep(finalx, finaly, directions, curx, cury - 1)
    elif directions[0][0] == 'L':
        pop = directions.pop(0)
        if int(pop[1:]) > 1:
            directions.insert(0, pop[0] + str(int(pop[1:])-1))
        return 1 + moveStep(finalx, finaly, directions, curx - 1, cury)
    elif directions[0][0] == 'R':
        pop = directions.pop(0)
        if int(pop[1:]) > 1:
            directions.insert(0, pop[0] + str(int(pop[1:])-1))
        return 1 + moveStep(finalx, finaly, directions, curx + 1, cury)

totalsteps = []
for isect in icoords:
    print(isect)
    totalsteps.append(moveStep(int(isect.split(',')[0]), int(isect.split(',')[1]), wire1.copy(), 0, 0) + moveStep(int(isect.split(',')[0]), int(isect.split(',')[1]), wire2.copy(), 0, 0))

print(totalsteps)
