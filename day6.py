file = open("input/day6.txt")
tuples = []
for line in file:
    pair = line.split(", ")
    tuples.append((int(pair[0]), int(pair[1])))
print(tuples)
