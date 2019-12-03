inputfile = open('input.txt', 'r')
wire1 = inputfile.readline().strip().split(',')
wire2 = inputfile.readline().strip().split(',')

wire1coords = []
wire2coords = []

x = 0
y = 0
for direction in wire1:
    if direction[0] == 'U':
        for count in range(int(direction[1:])):
            y += 1
            wire1coords.append(f'{x},{y}')
    elif direction[0] == 'D':
        for count in range(int(direction[1:])):
            y -= 1
            wire1coords.append(f'{x},{y}')
    elif direction[0] == 'L':
        for count in range(int(direction[1:])):
            x -= 1
            wire1coords.append(f'{x},{y}')
    elif direction[0] == 'R':
        for count in range(int(direction[1:])):
            x += 1
            wire1coords.append(f'{x},{y}')
print('computed coords for wire1', len(wire1coords))


x = 0
y = 0
for direction in wire2:
    if direction[0] == 'U':
        for count in range(int(direction[1:])):
            y += 1
            wire2coords.append(f'{x},{y}')
    elif direction[0] == 'D':
        for count in range(int(direction[1:])):
            y -= 1
            wire2coords.append(f'{x},{y}')
    elif direction[0] == 'L':
        for count in range(int(direction[1:])):
            x -= 1
            wire2coords.append(f'{x},{y}')
    elif direction[0] == 'R':
        for count in range(int(direction[1:])):
            x += 1
            wire2coords.append(f'{x},{y}')
print('computed coords for wire2', len(wire2coords))


print('compupting intersects...')
intersects = []

for coord in wire1coords:
    if coord in wire2coords:
        intersects.append(coord)
        print(f'intersect! {coord}')

print('computing Manhattan distance...')
for i in range(len(intersects)):
    intersects[i] = int(intersects[i].split(',')[0]) + int(intersects[i].split(',')[1])

print('finding smallest distance...')
lowest = intersects[0]
for distance in intersects:
    if distance < lowest:
        lowest = distance

print(lowest)
