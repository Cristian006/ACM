
def eggdrop(inputFile):
    f = open(inputFile)
    nStr, kStr = f.readline().split(" ")
    n, k = int(nStr), int(kStr)

    data = []
    for i in range(n):
        floorNum, state = f.readline().split(' ')
        floorNum = int(floorNum)
        state = state.strip()
        data.append((floorNum, state))
    data.append((1,"SAFE"))
    data.append((k, "BROKEN"))

    # highest safe floor
    lcb = 0
    # lowest broken floor
    hmnb = k+1

    for floor, state in data:
        if state == "SAFE":
            if floor > lcb:
                lcb = floor
        else:
            if floor < hmnb:
                hmnb = floor


    lcb += 1 # highest safe value +1
    hmnb -= 1 # lowest broken value - 1

    return str(lcb) +" "+ str(hmnb)

if __name__ == "__main__":
    r = eggdrop("C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\EggDrop\\input\\EggDrop-1006.in")
