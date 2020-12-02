# day 1, part 2
inputlines = []
inputfile = open('input.txt', 'r')
for line in inputfile:
    inputlines.append(int(line))

#print(inputlines)
#print("Length: " + str(len(inputlines)))

num1 = 0
num2 = 1
num3 = 2

while (inputlines[num1] + inputlines[num2] + inputlines[num3]) != 2020:
    #print("Tried " + str(inputlines[num1]) + ", " + str(inputlines[num2]) + ", " + str(inputlines[num3]))
    #print("Tried " + str(num1) + ", " + str(num2) + ", " + str(num3))
    num3 += 1
    if num3 == len(inputlines):
        num2 += 1
        if num2 == len(inputlines) - 1:
            num1 += 1
            num2 = num1 + 1
        num3 = num2 + 1

print(inputlines[num1] * inputlines[num2] * inputlines[num3])