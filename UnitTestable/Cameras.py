def cameras(fileName):
    f = open(fileName, 'r')
    info = f.readline()
    nStr, kStr, rStr = info.split(' ')
    n, k, r = int(nStr), int(kStr), int(rStr)
    minNumHouses = 2
    cameraHouses = [0] * n

    cameraAdditions = 0
    line = f.readline()
    for i in range(k):
        cameraHouse = int(line)
        cameraHouses[cameraHouse - 1] = 1
        line = f.readline()

    for i in range(n):
        nextNumHousesWithCameras = sum(cameraHouses[i:i + r])

        if nextNumHousesWithCameras < minNumHouses:
            neededInstall = minNumHouses - nextNumHousesWithCameras
            rightMostIndex = i + r - 1
            if i + r > len(cameraHouses):
                break
            if neededInstall == 1:
                if cameraHouses[rightMostIndex] != 1:
                    cameraHouses[rightMostIndex] = 1
                else:
                    cameraHouses[rightMostIndex - 1] = 1
                cameraAdditions += 1
            else:
                cameraHouses[rightMostIndex] = 1
                cameraHouses[rightMostIndex - 1] = 1
                cameraAdditions += 2

    return cameraAdditions