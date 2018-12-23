file = open("input/day7.txt")
prereqs = {}
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for letter in alphabet:
    prereqs[letter] = []
for line in file:
    split = line.split(" ")
    prereqs[split[7]].append(split[1])
print(prereqs)
