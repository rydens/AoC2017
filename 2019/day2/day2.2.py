inputfile = open('input.txt', 'r')
initints = []
for num in inputfile.readline().split(','):
    initints.append(int(num))


def execute(initints, noun, verb): 
    ints = initints.copy()
    ints[1] = noun
    ints[2] = verb
    for i in range(0, len(ints), 4):
        print(i)
        if ints[i] == 1:
            ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
        elif ints[i] == 2:
            ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
        elif ints[i] == 99:
            break
    return [ints[0], ints[1], ints[2]]

output = execute(initints, 0, 0)
initnoun = 0
initverb = 0
while output[0] != 19690720:
    initnoun += 1
    if initnoun == 100:
        initnoun = 0
        initverb += 1
    output = execute(initints, initnoun, initverb)

print(output)
print(100 * output[1] + output[2])
