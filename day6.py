file = open("input/day6.txt")
tuples = []
for line in file:
    pair = line.split(", ")
    tuples.append((int(pair[0]), int(pair[1])))
for x in range(0, 400):
    for y in range(0, 400):
        if (x, y) in tuples:
            print("X", end="")
        else:
            print("O", end="")
    print("")
