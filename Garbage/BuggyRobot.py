
f = open('', 'r')
# get n and m
n = int(f.read(1))
f.seek(2)
m = int(f.read(1))
f.seek(5)

# create the matrix
M = [[None] * m for i in range(n)]
start = [0, 0]
end = [0, 0]

# build it
for r in range(n):
    for c in range(m):
        M[r][c] = f.read(1)
        # record start and end positions
        if M[r][c] == 'R':
            start[0] = r
            start[1] = c
        elif M[r][c] == 'E':
            end[0] = r
            end[1] = c

    f.read(1)

commandStr = f.readline()

# close file
f.close()

def xValInRange(x): return 0 <= x < n
def yValInRange(y): return 0 <= y < m
def isTraversable(command, current):
    if command == 'R' and xValInRange(current[0]+1) and M[current[0]][current[1]+1] == '.':
        return True
    elif command == 'L' and xValInRange(current[0]-1)and M[current[0]][current[1]-1] == '.':
        return True
    elif command == 'U' and yValInRange(current[1]-1) and M[current[0]-1][current[1]] == '.':
        return True
    elif command =='D' and yValInRange(current[1]+1) and M[current[0]+1][current[1]] == '.':
        return True
    else:
        print("Not valid   ignore")


robot_position = start
for command in commandStr:
    if isTraversable(command, robot_position):
        print("Traverse")
    else:
        print("Dont traverse")
