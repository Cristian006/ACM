S = "abcdecdee"
T = "ace"

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
    print("NADA")
else:
    print(countSubsequence(0, m, m[0][0], 0, True))