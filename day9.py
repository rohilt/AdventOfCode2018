import csv

class CircularList:
    def __init__(self):
        self.list = []
        self.curr = 0
    def toggleClockwise(self, q):
        self.curr += (q % len(self.list))
        if self.curr > len(self.list):
            self.curr -= len(self.list)
        if len(self.list) == 1:
            self.curr = 1
    def toggleCounterClockwise(self, q):
        self.curr -= (q % len(self.list))
        if self.curr <= 0:
            self.curr += len(self.list)

class PlayersList:
    def __init__(self):
        CircularList.__init__(self)
        for x in range(410):
            self.list.append(0)
    def nextPlayer(self):
        self.curr += 1
        if self.curr >= len(self.list):
            self.curr -= len(self.list)
    def addPlayerScore(self, q):
        self.list[self.curr] += q

class MarbleGame(CircularList):
    def __init__(self):
        CircularList.__init__(self)
        self.list.append(0)
        self.currNumber = 0
    def playerTurn(self):
        self.currNumber += 1
        if self.currNumber % 23 == 0:
            self.toggleCounterClockwise(7)
            if self.curr == len(self.list):
                self.curr = 0
            popped = self.list.pop(self.curr)
            return self.currNumber + popped
        else:
            self.toggleClockwise(2)
            self.list.insert(self.curr, self.currNumber)
            return 0

file = open("output/day9.csv", mode = 'w')
writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for x in range(10000):
    players = PlayersList()
    game = MarbleGame()
    while game.currNumber <= x:
        players.addPlayerScore(game.playerTurn())
        players.nextPlayer()
    writer.writerow([x, max(players.list)])
    print(x)
file.close()
