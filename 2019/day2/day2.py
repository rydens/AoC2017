inputfile = open('input.txt', 'r')
ints = []
for num in inputfile.readline().split(','):
    ints.append(int(num))

ints[1] = 12
ints[2] = 2

for i in range(0, len(ints), 4):
    print(i)
    if ints[i] == 1:
        ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
    elif ints[i] == 2:
        ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
    elif ints[i] == 99:
        break

print(ints[0])
