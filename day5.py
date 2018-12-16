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
letters = file.read()
polymer = []
count = 0
for letter in letters:
    polymer.append(letter)
    removeIfNeeded(polymer)
    if count > 100:
        break
print(len(polymer)) # Part A Solution, but 1 higher than actual answer (\n or null terminator)?
file.close()
