inputRange = [246515, 739105]

nums = []

def adjCheck(num):
    num = str(num)
    i = 0
    while i < len(num) - 1:
        if num[i] == num[i+1] and num.count(num[i]) == 2:
            return True
        i += 1
    return False

def incCheck(num):
    num = str(num)
    i = 0
    while i < len(num) - 1:
        if int(num[i]) > int(num[i+1]):
            return False
        i += 1
    return True

for i in range(inputRange[0], inputRange[1]):
    if not adjCheck(i):
        continue
    elif not incCheck(i):
        continue
    print(i)
    nums.append(i)

print(len(nums))
