from sys import argv

inputfile = open(argv[-1], 'r')
initints = []
for num in inputfile.readline().split(','):
    initints.append(int(num))

# Opcodes:
# 0 x x 01: (param1 + param2, stores in pos param3)
# 0 x x 02: (param1 * param2, stores in pos param3)
# 0 03: single int input, saves it to pos param1
# 0 04: outputs value at pos param1
# 99: immediate program halt

def opExec(opcode):
    print(opcode)
    paramTypes = str(opcode)[::-1][2:]
    opcode = int(str(opcode)[-2:])
    
    if (opcode == 1):
        paramTypes += '0'*(3-len(paramTypes))
        params = list(map(lambda p, ptype: str(p) if ptype == '0' else p, initints[i+1:i+len(paramTypes)+1], paramTypes))
        print(params)
        p0 = initints[int(params[0])] if type(params[0]) == str else params[0]
        p1 = initints[int(params[1])] if type(params[1]) == str else params[1]
        initints[int(params[-1])] = p0 + p1

        return len(paramTypes) + 1

    elif (opcode == 2):
        paramTypes += '0'*(3-len(paramTypes))
        params = list(map(lambda p, ptype: str(p) if ptype == '0' else p, initints[i+1:i+len(paramTypes)+1], paramTypes))

        p0 = initints[int(params[0])] if type(params[0]) == str else params[0]
        p1 = initints[int(params[1])] if type(params[1]) == str else params[1]
        initints[int(params[-1])] = p0 * p1

        return len(paramTypes) + 1

    elif (opcode == 3):
        paramTypes += '0'
        params = list(map(lambda p, ptype: str(p) if ptype == '0' else p, initints[i+1:i+len(paramTypes)+1], paramTypes))
        print(paramTypes, params)
        initints[int(params[0])] = int(input('> '))

        return len(paramTypes) + 1

    elif (opcode == 4):
        paramTypes += '0'
        params = list(map(lambda p, ptype: str(p) if ptype == '0' else p, initints[i+1:i+len(paramTypes)+1], paramTypes))

        print(initints[int(params[0])])

        return len(paramTypes) + 1

    elif (opcode == 99):
        return len(initints)

    else:
        print(f'GOD IS DEAD: {opcode}')
        exit()



i = 0
while i < len(initints):
    i += opExec(initints[i])
