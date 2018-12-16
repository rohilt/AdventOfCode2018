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
print(len(letters))
polymer = []
for letter in letters:
    polymer.append(letter)
    removeIfNeeded(polymer)
print(len(polymer))
