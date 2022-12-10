print("*********************************")
print("\tAOC 2022 - Day 06")
print("*********************************")


with open('input.txt') as f:
    string = f.read()


# Part 1
def Part1():
    seq = []
    for i in range(len(string)):
        seq.append(string[i])

        if len(seq) == 4:
            for j in seq:
                if seq.count(j) != 1:
                    dup = True
                    break
                else:
                    dup = False

            if dup == False:
                print("Start-of-packet marker:")
                return i+1
            else:
                seq.pop(0) 


# Part 2
def Part2():
    seq = []
    for i in range(len(string)):
        seq.append(string[i])

        if len(seq) == 14:
            for j in seq:
                if seq.count(j) != 1:
                    dup = True
                    break
                else:
                    dup = False

            if dup == False:
                print("Start-of-message marker:")
                return i+1
            else:
                seq.pop(0) 

if __name__ == '__main__':
    print(Part1())
    print(Part2())
