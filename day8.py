# Node Class defined
class Node:
    def __init__(self):
        self.meta = []
        self.children = []
    def setMeta(self, meta):
        self.meta = meta
    def setChildren(self, children):
        self.children = children
    def getValue(self):
        sum = 0
        if len(self.children) == 0:
            for x in self.meta:
                sum += x
        else:
            for x in self.meta:
                if x <= len(self.children):
                    sum += self.children[x - 1].getValue()
        return sum

# Input processing
loc = 0
input = open("input/day8.txt")
data = []
for line in input:
    for x in line.split(' '):
        data.append(x)
input.close()

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
    node = Node()
    for x in range(numChilds):
        node.children.append(generateNode())
    for x in range(numMeta):
        node.meta.append(readNext())
    return node

# Part B
baseNode = generateNode()
print(baseNode.getValue())
