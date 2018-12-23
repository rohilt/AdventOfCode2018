# Node Class defined
class Node:
    def __init__(self, meta):
        self.sum = 0
        for x in meta:
            self.sum += x

# Input processing
loc = 0
input = open("input/day8.txt")
data = []
for line in input:
    for x in line.split(' '):
        data.append(x)
input.close()
nodes = []

# Helper Function
def readNext():
    global loc
    global data
    loc += 1
    return int(data[loc-1])

# Generate node
def generateNode():
    global loc
    meta = []
    numChilds = readNext()
    numMeta = readNext()
    for x in range(numChilds):
        generateNode()
    for x in range(numMeta):
        meta.append(readNext())
    nodes.append(Node(meta))

generateNode()
sum = 0
for x in nodes:
    sum += x.sum
print(sum)
