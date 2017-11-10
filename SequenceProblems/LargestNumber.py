arr = ['99999', '9', '888888', '9919', '01', '12', '19']

def breakTie(arr, i, j):
    n1 = arr[i]
    n2 = arr[j]
    n1L = len(n1)
    n2L = len(n2)
    l = n1L if n1L < n2L else n2L
    for k in range(l):
        if n1[k] > n2[k]:
            return i
        elif n1[k] < n2[k]:
            return j

    if n1L < n2L:
        return i
    else:
        return j


maxNumArr = []
for i in range(len(arr)):
    cm = 0
    while arr[cm] is None:
        cm += 1

    for j in range(len(arr)):
        if arr[j] is None:
            continue

        if arr[cm][0] < arr[j][0]:
            cm = j
        elif arr[cm][0] == arr[j][0] and cm != j:
            cm = breakTie(arr, cm, j)

    maxNumArr.append(arr[cm])
    arr[cm] = None


print(maxNumArr)
