def excellence(inputFile):
    f = open(inputFile)
    n = int(f.readline().strip())
    studentRatings = []
    for i in range(n):
        studentRatings.append(int(f.readline().strip()))

    studentRatings.sort()


    i, j = 0, len(studentRatings)-1
    sumOfPairs = []
    while i < j:
        sumOfPairs.append(studentRatings[i] + studentRatings[j])
        i += 1
        j -= 1

    return min(sumOfPairs)


if __name__ == "__main__":
    o = excellence('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Excellence\\input\\Excellence-1000.in')

