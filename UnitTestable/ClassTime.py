import operator

def classtime(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    names = []
    for i in range(n):
        fn, ln = f.readline().split(' ')
        ln = ln.strip()
        names.append([fn, ln])
    f.close()

    # this allows sort via multiple criterion; super cool
    # in this case we sort by last name first then by first name
    names = sorted(names, key=operator.itemgetter(1,0))
    namesStr = ''
    for f, l in names:
        namesStr += f+' '+l+'\n'

    return namesStr

def correctOutput(outputFile):
    f = open(outputFile)
    names = f.readlines()
    f.close()
    return names


if __name__ == "__main__":
    o = classtime('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\ClassTime\\input\\ClassTime-1000.in')
    #co = correctOutput('C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\ClassTime\\output\\ClassTime-1000.out')
    # print(o)