import time

f = open("CameraData.txt", 'r')
info = f.readline()
nStr, kStr, rStr = info.split(' ')
n, k, r = int(nStr), int(kStr), int(rStr)
minNumHouses = 2
cameraHouses = [0] * n

start = time.time()

cameraAdditions = 0
line = f.readline()
while line:
    cameraHouse = int(line)
    cameraHouses[cameraHouse] = 1
    line = f.readline()

for i in range(0, n, r):
    nextNumHousesWithCameras = sum(cameraHouses[i:i + r])
    if nextNumHousesWithCameras < minNumHouses:
        if len(cameraHouses[i:i + r]) >= minNumHouses:
            cameraAdditions += minNumHouses - nextNumHousesWithCameras

print(cameraAdditions)

print(time.time() - start)