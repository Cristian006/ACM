def complexity(inputFile):
    f = open(inputFile)
    seq = f.readline().strip()
    maxComplexity = 2
    freqMap = {}

    for letter in seq:
        if letter in freqMap:
            freqMap[letter] += 1
        else:
            freqMap[letter] = 1

    sortedKeys = sorted(freqMap.keys(), key=lambda x: freqMap[x], reverse=False)
    currentComplexity = len(sortedKeys)
    numberDeletions = 0
    i = 0

    while currentComplexity > maxComplexity:
        currentComplexity -= 1
        numberDeletions += freqMap[sortedKeys[i]]
        i+=1

    return numberDeletions

if __name__ == "__main__":
    print(complexity("C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\Complexity\\input\\Complexity-1020.in"))