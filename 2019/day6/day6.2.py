inputfile = open('input.txt', 'r')

orbitMap = []

for orbit in inputfile:
    orbitMap.append(orbit.strip())

def search(string):
    for i in orbitMap:
        if i.endswith(string):
            return i

def trace(orbit1, path, end='COM'):
    path.append(orbit1)
    if orbit1.split(')')[0] == end:
        return path
    return trace(search(orbit1.split(')')[0]), path, end)



pathYOU = trace(search('YOU'), [])
print(pathYOU)
pathSAN = trace(search('SAN'), [])
print(pathSAN)

x = 0
y = 0
while pathYOU[x].split(')')[0] != pathSAN[y].split(')')[0]:
    x += 1
    if x == len(pathYOU):
        x = 0
        y += 1

print(pathYOU[x].split(')')[0])
print(len(trace(search('YOU'), [], pathYOU[x].split(')')[0])[1:]) + len(trace(search('SAN'), [], pathSAN[y].split(')')[0])[1:]))
