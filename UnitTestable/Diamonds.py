def getSubsequenceCount(data):
    sequence = [1] * len(data)
    for i in range(1, len(data)):
        for j in range(i):
            if data[j] > data[i]:
                sequence[i] = sequence[j]+1
    print(sequence)
    return max(sequence)

numOfD = int(input())
d = []
for i in range(numOfD):
    w, c  = input().split(" ")
    w = float(w)
    c = float(c)
    v = float("inf")
    if w == 0 and c == 0:
        continue
    elif w != 0:
        if c != 0:
            v = c / w
        else:
            v = -1 * w
    print(v)
    d.append(v)

print(getSubsequenceCount(d))