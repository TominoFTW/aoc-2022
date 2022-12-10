print("*********************************")
print("\tAOC 2022 - Day 2")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()


# Part 1
myChoice = {'X': 1, 'Y': 2, 'Z': 3}
combos = {'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 6, 'C Y': 0, 'C Z': 3}
score = 0

for line in lines:
    score += myChoice[line[2]] + combos[line]

print("Score from logic")
print(score)


# Part 2
myChoice = {'X': 1, 'Y': 2, 'Z': 3}
combos = {'A X': 'Z', 'A Y': 'X', 'A Z': 'Y', 'B X': 'X', 'B Y': 'Y', 'B Z': 'Z', 'C X': 'Y', 'C Y': 'Z', 'C Z': 'X'}
perRoundPoints = {'X': 0, 'Y': 3, 'Z': 6}


score = 0
for line in lines:
    score += perRoundPoints[line[2]] + myChoice[combos[line]]

print("Score from instructions")
print(score)
