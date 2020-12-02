from sys import argv

inputfile = open(argv[-1], 'r')
program = []
for num in inputfile.readline().split(','):
    program.append(int(num))

# Opcodes:
# 0 x x 01: (param1 + param2, stores in pos param3)
# 0 x x 02: (param1 * param2, stores in pos param3)
# 0 03: single int input, saves it to pos param1
# 0 04: outputs value at pos param1
# 99: immediate program halt


def _99(p, m=''):
    exit()

def _01(p, m='000'):
    program[p[2]] = (program[p[0]] if m[0] == '0' else p[0]) + (program[p[1]] if m[1] == '0' else p[1])
    global i 
    i += 4

def _02(p, m='000'):
    program[p[2]] = (program[p[0]] if m[0] == '0' else p[0]) * (program[p[1]] if m[1] == '0' else p[1])
    global i
    i += 4

def _03(p, m='0'):
    program[p[0]] = int(input('> '))
    global i
    i += 2

def _04(p, m='0'):
    print(program[p[0]] if m[0] == '0' else p[0])
    global i
    i += 2


ops = {
    99: (_99, 0),
    1: (_01, 3),
    2: (_02, 3),
    3: (_03, 1),
    4: (_04, 1)
}

i = 0
while i < len(program):
    opcode = int(str(program[i])[-2:])
    #print(program[i], opcode)
    #instruction = program[i:i+ops[opcode][1]+1]
    #print(instruction)
    #modes = str(instruction[0])[::-1][2:]
    #print(modes)
    #print()
    ops[opcode][0](program[i+1:i+ops[opcode][1]+1], str(program[i])[::-1][2:].ljust(ops[opcode][1], '0'))
