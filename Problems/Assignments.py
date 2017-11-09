def assignments(inputFile, outputFile):

    f = open(inputFile,'r')
    outputFile = open(outputFile,'r')

    outStr = ""


    n = int(f.readline())


    shipsDeployedFromEachDock = []

    for _ in range(n):
          outStr += outputFile.readline()
          shipCount, dist = f.readline().split(" ")
          shipCount = int(shipCount)
          dist = int(dist)
          shipsDeployed = 0


          #Have to do while, since it does ship count, then ships, then ship count again.
          for _ in range(shipCount):
              topSpeed, fuel, fuelConsumption = f.readline().split(" ")
              topSpeed = int(topSpeed)
              fuel = int(fuel)
              fuelConsumption = int(fuelConsumption)

              fuelNeeded = float(dist) / float(topSpeed)
              fuelNeeded *= float(fuelConsumption)

              if fuelNeeded <= fuel:
                  shipsDeployed += 1

          shipsDeployedFromEachDock.append(shipsDeployed)



    shipsDeployedStr = ""
    for shipsDeployed in shipsDeployedFromEachDock:
        shipsDeployedStr += (str(shipsDeployed) + "\n")

    return shipsDeployedStr == outStr





if (assignments("..\\UnitTests\\_IO_Div2_2013\\Assignments.in","..\\UnitTests\\_IO_Div2_2013\\Assignments.out")):
    print("matched unit test")

