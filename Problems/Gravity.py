def gravity(filePath):
    f = open(filePath, 'r')
    info = f.readline()
    rStr, cStr = info.split(' ')
    r, c = int(rStr), int(cStr)

    line = f.readline()
    M = []
    for i in range(r):
        M.append(list(line.strip()))
        line = f.readline()

    def rValInRange(y): return 0 <= y < r

    for cols in range(c):
        for rows in range(r-1, -1, -1):
            if M[rows][cols] == 'o':
                currentRow = rows
                while rValInRange(currentRow+1) and M[currentRow+1][cols] == '.':
                    M[currentRow][cols] = '.'
                    M[currentRow+1][cols] = 'o'
                    currentRow += 1

    print(M, '\n\n')
    MStr = ''
    for row in M:
        print(row)
        MStr += ''.join(row) + '\n'
    return MStr

