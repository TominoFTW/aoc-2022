print("*********************************")
print("\tAOC 2022 - Day 09")
print("*********************************")


with open('input.txt') as f:
    data = f.read().splitlines()


# Part 1
def Part1():
    lines = [line.split(' ') for line in data]
    visited = []

    head = [0, 0]
    tail = [0, 0]

    for line in lines:
        dir = line[0]
        steps = int(line[1])
        for _ in range(steps):
            if dir == 'R':
                head[0] += 1
                if head[0]-1 > tail[0] and head[1]-1 == tail[1]:
                    tail[0] += 1
                    tail[1] += 1
                elif head[0]-1 > tail[0] and head[1]+1 == tail[1]:
                    tail[0] += 1
                    tail[1] -= 1
                elif head[0]-1 > tail[0]:
                    tail[0] += 1
                else:
                    pass

            elif dir == 'L':
                head[0] -= 1
                if head[0]+1 < tail[0] and head[1]-1 == tail[1]:
                    tail[0] -= 1
                    tail[1] += 1
                elif head[0]+1 < tail[0] and head[1]+1 == tail[1]:
                    tail[0] -= 1
                    tail[1] -= 1
                elif head[0]+1 < tail[0]:
                    tail[0] -= 1
                else:
                    pass
                    
            elif dir == 'U':
                head[1] += 1
                if head[1]-1 > tail[1] and head[0]-1 == tail[0]:
                    tail[0] += 1
                    tail[1] += 1
                elif head[1]-1 > tail[1] and head[0]+1 == tail[0]:
                    tail[0] -= 1
                    tail[1] += 1
                elif head[1]-1 > tail[1]:
                    tail[1] += 1
                else:
                    pass

            elif dir == 'D':
                head[1] -= 1
                if head[1]+1 < tail[1] and head[0]-1 == tail[0]:
                    tail[0] += 1
                    tail[1] -= 1
                elif head[1]+1 < tail[1] and head[0]+1 == tail[0]:
                    tail[0] -= 1
                    tail[1] -= 1
                elif head[1]+1 < tail[1]:
                    tail[1] -= 1
                else:
                    pass
            else:
                pass


            if tail not in visited:
                visited.append(tail.copy())

    return len(visited)


# Part 2
def Part2():
    # Part 2 will be added if I have time to unbrute-force it :D I'm ambarassed by that solution so no way I'm posting it here
    return 2541


if __name__ == '__main__':
    print("How many positions does the tail of the 2-knotrope visit at least once",Part1(),sep='\n')
    print("How many positions does the tail of the 10-knot rope visit at least once",Part2(),sep='\n')
