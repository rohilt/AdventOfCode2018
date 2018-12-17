def removeIfNeeded(list):
    if len(list) < 2:
        return
    lastItem = list.pop()
    secondLastItem = list.pop()
    if (lastItem.islower() or secondLastItem.islower()) and (lastItem.isupper() or secondLastItem.isupper()) and lastItem.lower() == secondLastItem.lower():
        removeIfNeeded(list)
    else:
        list.append(secondLastItem)
        list.append(lastItem)
file = open("input/day5.txt")
lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = file.read()
polymer = []
count = 0
for letter in letters:
    polymer.append(letter)
    removeIfNeeded(polymer)
print(len(polymer)) # Part A Solution, but 1 higher than actual answer (\n or null terminator)?
file.close()
minLength = 100000000
for x in lettersList:
    polymer = []
    for y in letters:
        if y != x.lower() and y != x.upper():
            polymer.append(y)
            removeIfNeeded(polymer)
    if len(polymer) < minLength:
        minLength = len(polymer)
print(minLength) # Part B Solution?
