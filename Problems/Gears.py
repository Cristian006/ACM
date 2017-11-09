class Node(object):
    def __init__(self, p, r):
        self.children = []
        self.x = p[0]
        self.y = p[1]
        self.r = r
        self.rd = 1
        self.isInput = False
        self.isOutput = False

    @staticmethod
    def isConnected(n1, n2):
        return Node.distanceBetween(n1,n2) - (n1.r + n2.r) < 0.0001

    @staticmethod
    def distanceBetween(n1, n2):
        a2 = (n1.x - n2.x)**2
        b2 = (n1.y - n2.y)**2
        return (a2 + b2)**(1/2)

def gears(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    grs = []

    for i in range(n):
        xStr, yStr, rStr = f.readline().split(' ')
        x, y, r = int(xStr), int(yStr), int(rStr)
        gearNode = Node([x,y], r)
        grs.append(gearNode)

    grs[0].isInput = True
    inputGear = grs[0]
    grs[-1].isOutput = True
    outputGear = grs[-1]

    for g in grs:
        for g2 in grs:
            if g != g2 and Node.isConnected(g, g2):
                g.children.append(g2)





gears('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Gears\\input\\Gears-0003.in')