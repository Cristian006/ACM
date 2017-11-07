import random as r
rNums = [r.randint(-100,100) for __ in range(7)]
rNums.sort()
print(rNums)

currentMin = float("inf")
for i in range(len(rNums)-1):
    v = abs(rNums[i] - rNums[i+1])
    if v != 0 and v < currentMin:
        currentMin = v

print(currentMin)