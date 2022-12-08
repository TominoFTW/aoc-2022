print("*********************************")
print("\tAOC 2022 - Day 08")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()

trees = [[int(t) for t in row.strip()] for row in lines]

h, w = len(trees), len(trees[0])


# Part 1
def Part1():
    canSee = 0

    for i in range(h):
        column = [trees[x][i] for x in range(h)]

        for j in range(w):
            row = trees[j]
            tree = trees[j][i]
            canSee += (all(tr < tree for tr in row[:i]) or all(tr < tree for tr in row[i+1:])
            or all(tr < tree for tr in column[:j]) or all(tr < tree for tr in column[j+1:]))

    return canSee


# Part 2
def Part2():
    highScore = 0

    for i in range(h):
        column = [trees[x][i] for x in range(h)]
        
        for j in range(w):
            row = trees[j]
            tree = row[i]
            left  = next((tr for tr in range(1, i) if row[i - tr] >= tree), i)
            right = next((tr for tr in range(1, w - i) if row[i + tr] >= tree), w - i - 1)
            up    = next((tr for tr in range(1, j) if column[j - tr] >= tree), j)
            down  = next((tr for tr in range(1, h - j) if column[j + tr] >= tree), h - j - 1)
            highScore = max(highScore, left * right * up * down)

    return highScore


if __name__ == '__main__':
    print("How many trees are visible from outside the grid\n",Part1(), sep='')
    print("What is the highest scenic score possible for any tree\n",Part2(), sep='')
