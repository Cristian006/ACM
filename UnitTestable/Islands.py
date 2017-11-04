from collections import deque

class Vertex(object):
    Up, Down, Left, Right = 0, 1, 2, 3
    def __init__(self):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited = False

    def addEdge(self, edgeType, other):
        if edgeType == Vertex.Up:
            self.up = other
            other.down = self
        elif edgeType == Vertex.Down:
            self.down = other
            other.up = self
        elif edgeType == Vertex.Left:
            self.left = other
            other.right = self
        else:
            self.right = other
            other.left = self

    def __str__(self):
        return 'V'


def islands(filePath):
    f = open(filePath)
    rStr, cStr = f.readline().split(' ')
    r, c = int(rStr), int(cStr)
    L, C, W, V = 'L', 'C', 'W', 'V'

    M = []
    line = f.readline()
    for row in range(r):
        M.append(list(line.strip()))
        line = f.readline()

    def xValInRange(x):
        return 0 <= x < c
    def yValInRange(y):
        return 0 <= y < r

    def isLandAdj(r, c):
        return (xValInRange(c-1) and M[r][c-1] == L) or+\
           (xValInRange(c+1) and M[r][c+1] == L) or+\
           (yValInRange(r-1) and M[r-1][c] == L) or+ \
           (yValInRange(r+1) and M[r+1][c] == L)

    def adjLands(r, c):
        connections = []
        if xValInRange(c - 1) and (M[r][c-1] == L or str(M[r][c-1]) == V):
            connections.append(Vertex.Left)
        if xValInRange(c+1) and (M[r][c+1] == L or str(M[r][c+1]) == V):
            connections.append(Vertex.Right)
        if yValInRange(r-1) and (M[r-1][c] == L or str(M[r-1][c]) == V):
            connections.append(Vertex.Up)
        if yValInRange(r+1) and (M[r+1][c] == L or str(M[r+1][c]) == V):
            connections.append(Vertex.Down)

        return connections

    def DFS(vertex):
        vertex.visited = True
        if vertex.up and vertex.up.visited == False:
            DFS(vertex.up)
        if vertex.down and vertex.down.visited == False:
            DFS(vertex.down)
        if vertex.left and vertex.left.visited == False:
            DFS(vertex.left)
        if vertex.right and vertex.right.visited == False:
            DFS(vertex.right)

    def toVertex(row, col, lands):
        newVertex = Vertex()
        queue.append(newVertex)
        M[row][col] = newVertex
        # making connections
        for edgeType in lands:
            if edgeType == Vertex.Left:
                otherVertex = M[row][col - 1]
                newVertex.addEdge(edgeType, otherVertex)
            elif edgeType == Vertex.Up:
                otherVertex = M[row - 1][col]
                newVertex.addEdge(edgeType, otherVertex)

    # this is the queue that is used to determine the number of islands
    # we just create a vertex everytime we see L
    queue = deque()
    for row in range(r):
        for col in range(c):
            if M[row][col] == C:
                lands = adjLands(row, col)
                if len(lands) > 0:
                    toVertex(row, col, lands)
                else:
                    M[row][col] = W
            elif M[row][col] == L:
                lands = adjLands(row, col)
                toVertex(row, col, lands)

    amountLands = 0
    if len(queue) == 0:
        return amountLands

    v = queue.popleft()
    while len(queue) > 0:
        amountLands += 1
        DFS(v)
        while v.visited:
            if len(queue) > 0:
                v = queue.popleft()
            else:
                break

    # if v and v.visited == False:
    #     DFS(v)
    #     amountLands += 1

    MStr = ''
    for row in M:
        for col in row:
            if col == 'W':
                MStr += str('o')
            elif str(col) == 'V':
                if col.visited:
                    MStr += str('u')
                else:
                    MStr += str('n')
            else:
                MStr += str('u')
        MStr += '\n'
    print(MStr)

    return amountLands


def getOutput(filePath):
    file = open(filePath, 'r')
    validOutputString = ''
    line = file.readline()
    while line:
        validOutputString += line
        line = file.readline()
    return validOutputString.strip()

if __name__ == "__main__":
    print("output:", islands('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Islands\\input\\Islands-1031.in'))
    print("valid output:", getOutput('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Islands\\output\\Islands-1031.out'))