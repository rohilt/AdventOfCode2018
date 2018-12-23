file = open("input/day7.txt")
prereqs = {}
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for letter in alphabet:
    prereqs[letter] = []
for line in file:
    split = line.split(" ")
    prereqs[split[7]].append(split[1])
result = []
while len(result) != len(prereqs):
    completed = True
    for letter in alphabet:
        if letter in result:
            continue
        completed = True
        for x in prereqs[letter]:
            if x not in result:
                completed = False
                print(x, end="")
                print(" not completed, so ", end="")
                print(letter, end="")
                print(" cannot be completed")
                break
        if completed:
            print(letter, end="")
            print(" completed")
            result.append(letter)
            break
        #if prereqs[letter] are all completed and in result
            #then place that letter next into completed/result, restart alphabet
for x in result:
    print(x, end="")
