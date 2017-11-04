
def distinctSubsequences(fileName):
    S = "abcdecdee"
    T = "ace"
    
    f = open(fileName, 'r')
    S = f.readline()
    T = f.readline()

    def countSubsequence(rowIndex, matrix, prevNum, subSeqCounter, isStart=False):
        if rowIndex == len(matrix):
            subSeqCounter += 1
            return subSeqCounter
        for i in matrix[rowIndex]:
            if i > prevNum or isStart:
                subSeqCounter = countSubsequence(rowIndex+1, matrix, i, subSeqCounter)
        return subSeqCounter

    def buildMap(S, T):
        numberMap = []
        for t in T:
            numberMap.append([])
            for i in range(len(S)):
                if S[i] == t:
                    numberMap[-1].append(i)
            if len(numberMap[-1]) == 0:
                numberMap.clear()
                return numberMap
        return numberMap

    m = buildMap(S, T)
    if len(m) == 0:
        return 0
    else:
        return countSubsequence(0, m, m[0][0], 0, True)