print("*********************************")
print("\tAOC 2022 - Day 10")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()

lines = [line.split() for line in lines]


# Part 1
def Part1():
    cycle = 1
    x = 1
    add = False
    toSum = [20, 60, 100, 140, 180, 220]

    j = 0
    line = lines[j]

    while(j+1 != len(lines)):
        if cycle in toSum:
            toSum[toSum.index(cycle)] = cycle * x

        if line[0] == 'addx':
            if add == True:
                x += int(line[1])
                add = False
            else:
                add = True

        if add == False:
            j += 1
            line = lines[j]

        cycle += 1

    return sum(toSum)


# Part 2
def Part2():
    cycle = 0
    sprite = [0,1,2]
    add = False

    j = 0
    line = lines[j]

    screen = [
                [],
                [],
                [],
                [],
                [],
                []
            ]


    while(j+1 != len(lines)):
        if cycle%40 in sprite:
            if cycle >= 0 and cycle <= 39:
                screen[0] += "#"
            elif cycle >= 40 and cycle <= 79:
                screen[1] += "#"
            elif cycle >= 80 and cycle <= 119:
                screen[2] += "#"
            elif cycle >= 120 and cycle <= 159:
                screen[3] += "#"
            elif cycle >= 160 and cycle <= 199:
                screen[4] += "#"
            elif cycle >= 200 and cycle <= 239:
                screen[5] += "#"
        else:
            if cycle >= 0 and cycle <= 39:
                screen[0] += " "
            elif cycle >= 40 and cycle <= 79:
                screen[1] += " "
            elif cycle >= 80 and cycle <= 119:
                screen[2] += " "
            elif cycle >= 120 and cycle <= 159:
                screen[3] += " " 
            elif cycle >= 160 and cycle <= 199:
                screen[4] += " " 
            elif cycle >= 200 and cycle <= 239:
                screen[5] += " " 
            

        if line[0] == 'addx':
            if add == True:
                sprite = [x+int(line[1]) for x in sprite]
                add = False
            else:
                add = True

        cycle += 1

        if add == False:
            j += 1
            line = lines[j]

    print("What eight capital letters appear on your CRT")
    for line in screen:
        print(' '.join(line))
    
    return "\nRGZEHURK"


if __name__ == '__main__':
    print("Sum of these six signal strengths",Part1(),sep='\n')
    print(Part2())
