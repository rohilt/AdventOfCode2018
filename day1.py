frequency = 0
firstIteration = True
map = {}
found = False
while not found:
    file = open("day1.txt")
    for line in file:
        if line[0]=="+":
            frequency += int(line[1:])
        else:
            frequency -= int(line[1:])
        if frequency not in map:
            map[frequency] = 1
        else:
            print(frequency) # Part B Solution
            found = True
            break
    if firstIteration:
        print(frequency) # Part A Solution
    firstIteration = False
    file.close()
