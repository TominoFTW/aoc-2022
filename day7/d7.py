print("*********************************")
print("\tAOC 2022 - Day 07")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()

stack = []
path = ''
dir_size = {}

space = 70000000
atleast = 30000000

# Part 1
def Part1():
    for line in lines:
        if line.startswith('$ cd'):
            if line == '$ cd /':
                path = '/'
                stack = [path]
            elif line == '$ cd ..':
                path = '/'.join(path.split('/')[:-1])
                stack.pop()
            else:
                path += '/' + line.split(' ')[2]
                stack.append(path)
        elif line[0].isdigit():
            for dir in stack:
                if dir not in dir_size.keys():
                    dir_size[dir] = 0
                dir_size[dir] += int(line.split(' ')[0])

    print("Total size of directories smaller than 100000")
    return sum([vals for vals in dir_size.values() if vals <= 100000])


# Part 2
def Part2():
    print("Smallest directory that can be deleted to fully free up space")
    return sorted([vals for vals in dir_size.values() if vals >= dir_size['/'] - 40000000])[0]


if __name__ == '__main__':
    print(Part1())
    print(Part2())
