from collections import deque
from math import ceil

def postman(inputFilePath):
    def clamp(v, minimum, maximum):
        return max(min(v, maximum), minimum)

    def carryRemainder(distances, distanceToLettersMap, index, rem, isLeft):
        v = distances.pop()
        if isLeft:
            distanceToLettersMap.pop(-v)
        else:
            distanceToLettersMap.pop(v)

        while rem > 0:
            index -= 1

            key = 0
            if isLeft:
                key = -distances[index]
            else:
                key = distances[index]

            if key == 0:
                return

            temp = rem
            rem -= distanceToLettersMap[key]
            distanceToLettersMap[key] -= temp
            if distanceToLettersMap[key] <= 0:
                distances.pop()


    dToLC = {}
    f = open(inputFilePath)
    nStr, kStr = f.readline().split(" ")
    n, k = int(nStr), int(kStr)

    for i in range(n):
        line = f.readline().split(" ")
        distance = int(line[0])
        numLetters = int(line[1])
        dToLC[distance] = numLetters

    distanceMapKeys = list(dToLC.keys())

    leftSide = [0]
    rightSide = [0]
    for num in distanceMapKeys:
        if num < 0:
            leftSide.append(abs(num))
        else:
            rightSide.append(num)

    leftSide.sort()
    rightSide.sort()


    def countingTotalDistance(list, isLeft):

        sortedDistances = deque(list)
        totalDistance = 0

        while len(sortedDistances) != 1:
            currentHouse = len(sortedDistances)-1
            ck = k

            key = 0
            if isLeft:
                key = -sortedDistances[currentHouse]
            else:
                key = sortedDistances[currentHouse]

            remainder = dToLC[key] % ck
            w = dToLC[key] / ck
            if remainder == 0:
                totalDistance += w * 2 * sortedDistances[currentHouse]
                sortedDistances.pop()
                dToLC.pop(key)
            elif w < 1: # more than enough
                totalDistance += 2 * sortedDistances[currentHouse]
                # error
                remainder = ck - dToLC[key]
                dToLC[key] = 0
                carryRemainder(sortedDistances, dToLC, currentHouse, remainder, isLeft)
            else: # Not enough
                totalDistance += 2 * sortedDistances[currentHouse]
                dToLC[key] -= ck

        return totalDistance

    td = countingTotalDistance(leftSide, True)
    td += countingTotalDistance(rightSide, False)
    return str(int(td))

if __name__ == "__main__":
    print( postman("C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\Postman\\input\\Postman-1002.in") )