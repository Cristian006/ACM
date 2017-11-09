from collections import deque

def grid(inputFile):
    f = open(inputFile)
    rStr, cStr = f.readline().split(' ')
    r, c = int(rStr), int(cStr)

    inf = float("inf")
    # up, down, left, right
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    directions = [None, None, None, None]

    M = [[None] * c for __ in range(r)]
    T = [[inf] * c for __ in range(r)]
    T[0][0] = 0

    # build grid
    for i in range(r):
        for j in range(c):
            M[i][j] = int(f.read(1))
        f.read(1)


    def inRange(row, col):
        if row >= 0 and row < r:
            if col >= 0 and col < c:
                return True
        return False

    def getValidDirections(i, j, directionsList):
        for k in range(4):
            ni = i + dx[k] * M[i][j]
            nj = j + dy[k] * M[i][j]
            if inRange(ni, nj):
                directionsList[k] = (ni, nj)
            else:
                directionsList[k] = None

    def BFS():
        q = deque([(0,0)])
        while len(q) > 0:
            # node stores current position
            node = q.popleft()
            ci, cy = node[0], node[1]
            getValidDirections(ci, cy, directions)
            for each in directions:
                if each:
                    i, j = each
                    if T[i][j] == inf:
                        T[i][j] = T[ci][cy] + 1
                        q.append(each)

        return T[-1][-1]

    n = BFS()
    return n if n != inf else "IMPOSSIBLE"


if __name__ == "__main__":
    v = grid('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Grid\\input\\Grid-1078.in')
    print(v)