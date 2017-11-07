# input
def zigzag(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    arr = [int(x) for x in f.readline().split(" ")]
    zigZagArr = [1] * n

    isIncreasing = True
    for i in range(1,len(arr)):
        isIncreasing = True
        for j in range(0,i):
            if isIncreasing:
                if arr[j] < arr[i]:
                    zigZagArr[i] = zigZagArr[j] + 1
            else:
                if arr[j] > arr[i]:
                    zigZagArr[i] = zigZagArr[j] + 1
            isIncreasing = not isIncreasing

    return zigZagArr[-1]

print(zigzag("C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\ZigZag\\input\\ZigZag-1065.in"))
