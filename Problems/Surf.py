class Node(object):
    def __init__(self):
        self.hic = False
        self.started = 0
        self.waitTime = 0
        self.dist = 0
        self.funPoints = 0
        self.children = []

    def at(self):
        return self.started + self.waitTime

def surf(inputFile):
    f = open(inputFile, 'r')
    n = int(f.readline())

    surfData = []
    for i in range(n):
        tStr, fpStr, wtStr = f.readline().split(' ')
        t, fp, wt = int(tStr), int(fpStr), int(wtStr)
        newNode = Node()
        newNode.started = t
        newNode.waitTime = wt
        newNode.funPoints = fp
        surfData.append( newNode )

    surfData.sort(key=lambda x: x.started)

    # graph construction
    for i in range(len(surfData)):
        for j in range(i+1, len(surfData)):
            if surfData[i].at() <= surfData[j].started:
                surfData[i].children.append(surfData[j])
                surfData[j].hic = True

    stack = []
    for node in surfData:
        if not node.hic:
            node.dist = node.funPoints
            stack.append(node)

    while len(stack) > 0:
        node = stack.pop()
        for child in node.children:
            if child.dist < node.dist + child.funPoints:
                child.dist = node.dist + child.funPoints
                stack.append(child)

    print(surfData[-1].dist)


if __name__ == "__main__":
    surf('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Surf\\input\\Surf-0001.in')
