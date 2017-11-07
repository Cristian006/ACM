passingCars = [0,1,0,1,1]

zeroCount = 0
totalPassingCars = 0
for v in passingCars:
    if v == 0:
        zeroCount += 1
    else:
        totalPassingCars += zeroCount

print(totalPassingCars)