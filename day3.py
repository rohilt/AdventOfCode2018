file = open("input\\day3.txt")
map = {}
for line in file:
    idSplit = line.split(" @ ")
    dimensionAndPositionSplit = idSplit[1].split(": ")
    positionSplit = dimensionAndPositionSplit[0].split(",")
    dimensionsSplit = dimensionAndPositionSplit[1].split("x")
    for i in range(int(positionSplit[0]), int(positionSplit[0]) + int(dimensionsSplit[0])):
        for j in range(int(positionSplit[1]), int(positionSplit[1]) + int(dimensionsSplit[1])):
            if (i, j) in map:
                map[(i, j)] = True
            else:
                map[(i, j)] = False
file.close()
file = open("input\\day3.txt")
for line in file:
    idSplit = line.split(" @ ")
    dimensionAndPositionSplit = idSplit[1].split(": ")
    positionSplit = dimensionAndPositionSplit[0].split(",")
    dimensionsSplit = dimensionAndPositionSplit[1].split("x")
    intact = True
    for i in range(int(positionSplit[0]), int(positionSplit[0]) + int(dimensionsSplit[0])):
        for j in range(int(positionSplit[1]), int(positionSplit[1]) + int(dimensionsSplit[1])):
            if map[(i, j)]:
                    intact = False
    if intact:
        print(idSplit[0][1:]) # Part B Solution
file.close()
count = 0
for tuple in map:
    if map[tuple]:
        count += 1
print(count) # Part A Solution
