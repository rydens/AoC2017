inputfile = open('input.txt', 'r')

orbitMap = []
for orbit in inputfile:
    orbitMap.append(orbit.strip())

def search(string):
    for i in orbitMap:
        if i.endswith(string):
            return i

def trace(orbit1):
    if orbit1.split(')')[0] == 'COM':
        return 1
    return 1 + trace(search(orbit1.split(')')[0]))

print(len(orbitMap))
tracker = 1

count = 0
for orbit in orbitMap:
    print(tracker, orbit)
    count += trace(orbit)
    tracker += 1

print(count)
