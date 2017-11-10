import operator

# submitted

def getMajority(a, data):
    tupleArr = []
    for each in a:
        tupleArr.append((data[each], each))
    tupleArr.sort(key=operator.itemgetter(0, 1))

    maxFreq = tupleArr[-1][0]
    answer = tupleArr[-1][1]
    for j in range(len(tupleArr) -1, -1, -1):
        if tupleArr[j][0] < maxFreq:
            break
        answer = tupleArr[j][1]

    print(answer)

numOfTestCases = int(input())
data = [0] * 1001
a = []
for i in range(numOfTestCases):
    subTestCases = int(input())
    for j in range(subTestCases):
        number = int(input())
        data[number] += 1
        a.append(number)
    getMajority(a, data)
    a.clear()
    data = [0] * 1001




