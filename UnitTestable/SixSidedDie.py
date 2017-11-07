
def gatherInput(inputFile):
    f = open(inputFile)
    playerOneDie = [int(x) for x in f.readline().split()]
    playerTwoDie = [int(x) for x in f.readline().split()]
    return playerOneDie, playerTwoDie

def sixsideddie(inputFile):
    pD1, pD2 = gatherInput(inputFile)

    w1, w2 = 0, 0
    for d1 in pD1:
        for d2 in pD2:
            if d1 > d2:
                w1 += 1
            elif d2 >  d1:
                w2 += 1

    answ = "%.5f" % round(w1/(w1+w2), 5)
    return answ



if __name__ == "__main__":
    a = sixsideddie("C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\SixSides\\input\\SixSides-0001.in")
    print(a)