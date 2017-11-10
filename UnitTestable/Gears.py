from math import gcd

class Node(object):
    def __init__(self, p, r):
        self.nbrs = []
        self.x = p[0]
        self.y = p[1]
        self.r = r
        self.rd = 0

    @staticmethod
    def isConnected(n1, n2):
        # instead of checking the the distance check distance squared
        return Node.distanceBetween(n1,n2) == (n1.r + n2.r)**2

    @staticmethod
    def distanceBetween(n1, n2):
        a2 = (n1.x - n2.x)**2
        b2 = (n1.y - n2.y)**2
        return a2 + b2

    def __str__(self):
        return "(" + str(self.x)+","+str(self.y) + ")"

def gears(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    grs = []

    for i in range(n):
        xStr, yStr, rStr = f.readline().split(' ')
        x, y, r = int(xStr), int(yStr), int(rStr)
        gearNode = Node([x,y], r)
        grs.append(gearNode)

    inputGear = grs[0]
    outputGear = grs[-1]

    # undirected graph is fully connected
    for g in grs:
        for g2 in grs:
            if g != g2 and Node.isConnected(g, g2):
                g.nbrs.append(g2)

    locked = False
    stack = []
    inputGear.rd = 1
    stack.append(inputGear)
    while len(stack) > 0:
        node = stack.pop()
        for c in node.nbrs:
            if c.rd == 0:
                c.rd = -node.rd
                stack.append(c)
            elif c.rd == node.rd:
                locked = True

    if locked:
        return 'The input gear cannot move.'
    elif grs[-1].rd == 0:
        return 'The input gear is not connected to the output gear.'
    else:
        ratio = gcd(inputGear.r, outputGear.r)
        inputGRatio = outputGear.r / ratio
        ogRatio = inputGear.r / ratio
        if inputGear.rd != outputGear.rd:
            ogRatio = -ogRatio
        return str(int(ogRatio)) +':'+str(int(inputGRatio))


#gears('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Gears\\input\\Gears-1006.in')