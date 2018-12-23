class Worker:
    def __init__(self):
        self.timeOccupied = 0
        self.letterAssigned = ''
    def assignStep(self, letter):
        self.letterAssigned = letter
        self.timeOccupied = ord(letter) - 4
    def passTime(self):
        if self.timeOccupied > 0:
            self.timeOccupied -= 1
    def completedStep(self):
        return self.timeOccupied == 0
    def returnStep(self):
        return self.letterAssigned

timeTaken = 0
workersIdle = [Worker() for x in range(5)]
workersBusy = []

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
    prereqsCompleted = True
    for letter in alphabet:
        workerAlreadyDoingStep = False
        for x in workersBusy:
            if x.letterAssigned == letter:
                workerAlreadyDoingStep = True
        if workerAlreadyDoingStep:
            continue
        if letter in result:
            continue
        prereqsCompleted = True
        for x in prereqs[letter]:
            if x not in result:
                prereqsCompleted = False
                break
        if prereqsCompleted and len(workersIdle) > 0:
            workerNowBusy = workersIdle.pop()
            workerNowBusy.assignStep(letter)
            workersBusy.append(workerNowBusy)
            if len(workersIdle) == 0:
                break
    for x in workersBusy:
        x.passTime()
    newWorkersBusy = []
    for x in workersBusy:
        if x.completedStep():
            result.append(x.returnStep())
            workersIdle.append(x)
        else:
            newWorkersBusy.append(x)
    workersBusy = newWorkersBusy
    timeTaken += 1
for x in result:
    print(x, end="") # Part A (used to be, see commit for Part 1)
print()
print(timeTaken) # Part B
