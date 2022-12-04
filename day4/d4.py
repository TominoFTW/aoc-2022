print("*********************************")
print("\tAOC 2022 - Day 4")
print("*********************************")

with open('input.txt') as f:
    lines = f.read().splitlines()


replaced = [line.replace('-',' ').replace(',',' ').split() for line in lines]


# Part 1
c = 0
sum = 0
for i in range(len(replaced)):
    st = [first for first in range(int(replaced[i][0]), int(replaced[i][1]) + 1)]
    nd = [second for second in range(int(replaced[i][2]), int(replaced[i][3]) + 1)]
    for j in st:
        for k in nd:
            if j == k:
                c += 1
                if c == len(st) or c == len(nd):
                    sum += 1
    c = 0

print("Sum of pairs does one range fully contain the other")
print(sum)


# Part 2
c = 0
sum = 0
for i in range(len(replaced)):
    st = [first for first in range(int(replaced[i][0]), int(replaced[i][1]) + 1)]
    nd = [second for second in range(int(replaced[i][2]), int(replaced[i][3]) + 1)]
    if st[0] <= nd[0] and st[-1] >= nd[-1]:
        sum += 1
    elif st[0] >= nd[0] and st[-1] <= nd[-1]:
        sum += 1
    elif st[0] <= nd[0] and st[-1] <= nd[-1]:
        if st[-1] >= nd[0]:
            sum += 1
    elif st[0] >= nd[0] and st[-1] >= nd[-1]:
        if nd[-1] >= st[0]:
            sum += 1

print("How many assignment pairs do the ranges overlap?")
print(sum)
