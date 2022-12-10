print("*********************************")
print("\tAOC 2022 - Day 5")
print("*********************************")

# Part 1
toBeLoaded = []
j = 0
with open('input.txt') as f:
    for line in f:
        if line.split()[0] == '1':
            numOfStacks = len(line.split())
            stacks = [[] for _ in range(numOfStacks + 1)]
            break
        line = line.rstrip("\n")
        for i in range((len(line) // 4) + 1):
            toBeLoaded.append(line[i * 4:(i + 1) * 4].strip().removeprefix("[").removesuffix("]"))

    for crate in toBeLoaded[-1::-1]:
        if crate == '':
            toBeLoaded.pop()
            continue
        if crate != '':
            break

    for i, crate in enumerate(toBeLoaded[-1::-1]):
        if j == numOfStacks:
            j = 0
        if crate == "":
            j += 1
            continue
        stacks[numOfStacks - j].insert(0, crate)
        j += 1

    lines = f.read().splitlines()
    lines.remove(lines[0])

    for stack in stacks:
        stack = stack[-1::-1]
            
    for line in lines:
        line = line.split()
        
        for moves in range(1,int(line[1])+1):
            stacks[int(line[5])].insert(0, stacks[int(line[3])].pop(0))

print("CrateMover 9000")
for stack in stacks:
    if stack == []:
        continue
    else:
        print(stack[0], end="")
        continue



# Part 2

toBeLoaded = []
j = 0
with open('input.txt') as f:
    for line in f:
        if line.split()[0] == '1':
            numOfStacks = len(line.split())
            stacks = [[] for _ in range(numOfStacks + 1)]
            break
        line = line.rstrip("\n")
        for i in range((len(line) // 4) + 1):
            toBeLoaded.append(line[i * 4:(i + 1) * 4].strip().removeprefix("[").removesuffix("]"))

    for crate in toBeLoaded[-1::-1]:
        if crate == '':
            toBeLoaded.pop()
            continue
        if crate != '':
            break

    for crate in toBeLoaded[-1::-1]:
        if j == numOfStacks:
            j = 0
        if crate == "":
            j += 1
            continue
        stacks[numOfStacks - j].insert(0, crate)
        j += 1

    lines = f.read().splitlines()
    lines.remove(lines[0])

    for stack in stacks:
        stack = stack[-1::-1]
            
    for line in lines:
        line = line.split()
        tmp = []
        for moves in range(1,int(line[1])+1):
            tmp.append(stacks[int(line[3])].pop(0))
        for i in tmp[-1::-1]:
            stacks[int(line[5])].insert(0, i)

print("\nCrateMover 9001")
for stack in stacks:
    if stack == []:
        continue
    else:
        print(stack[0], end="")
