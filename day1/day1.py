print("*********************************")
print("\tAOC 2022 - Day 1")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()
lines.append('')


# Part 1
elfSum = 0
getMax = 0
for line in lines:
    if line == '':
        getMax = max(getMax, elfSum)
        elfSum = 0
    else:
        elfSum += int(line)

print("Elf with the most calories")        
print(getMax)


# Part 2
elfSum = 0
getFirst = 0
getSecond = 0
getThird = 0

for line in lines:
    if line == '':
        if elfSum > getFirst:
            getThird, getSecond, getFirst = getSecond, getFirst, elfSum
        elif elfSum > getSecond:
            getThird, getSecond = getSecond, elfSum
        elif elfSum > getThird:
            getThird = elfSum
        elfSum = 0
    else:
        elfSum += int(line)

print("Sum of the first 3 elves")      
print(getFirst + getSecond + getThird)
