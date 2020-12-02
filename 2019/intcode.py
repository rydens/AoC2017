from sys import argv

program = []

if argv[-1].endswith('txt'):
    inputfile = open(argv[-1], 'r')
    for num in inputfile.readline().split(','):
        program.append(int(num))
elif argv[-1]:
    for num in argv[-1].split(','):
        program.append(int(num))
else:
    print('day5.py <file.txt|"program">')
    exit()

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

def _05(p, m='00'):
    global i
    i = (program[p[1]] if m[1] == '0' else p[1]) if (program[p[0]] if m[0] == '0' else p[0]) != 0 else i + 3

def _06(p, m='00'):
    global i
    i = (program[p[1]] if m[1] == '0' else p[1]) if (program[p[0]] if m[0] == '0' else p[0]) == 0 else i + 3

def _07(p, m='000'):
    program[p[2]] = 1 if ((program[p[0]] if m[0] == '0' else p[0]) < (program[p[1]] if m[1] == '0' else p[1])) else 0
    global i
    i += 4

def _08(p, m='000'):
    program[p[2]] = 1 if ((program[p[0]] if m[0] == '0' else p[0]) == (program[p[1]] if m[1] == '0' else p[1])) else 0
    global i
    i += 4


ops = {
    99: (_99, 0),   # Halth
    1: (_01, 3),    # Addition
    2: (_02, 3),    # Multiplication
    3: (_03, 1),    # User input
    4: (_04, 1),    # Output
    5: (_05, 2),    # jump-if-true
    6: (_06, 2),    # jump-if-false
    7: (_07, 3),    # less than
    8: (_08, 3)     # equals
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
