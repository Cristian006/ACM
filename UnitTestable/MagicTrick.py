
def magictrick(fileInput):
    f = open(fileInput)
    n = int(f.readline())
    data = []

    for i in range(n):
        data.append(f.readline().split(" "))

    numFuckUps = 0
    for i in range(1,101):
        number = i
        for operation, operand in data:
            operand = int(operand)
            if operation == "ADD":
                number += operand
            elif operation == "SUBTRACT":
                number -= operand
            elif operation == "DIVIDE":
                number /= operand
            else:
                number *= operand

            if number < 0 or number % 1 != 0:
                numFuckUps += 1
                break

    return numFuckUps



if __name__ == "__main__":
    print(magictrick("C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\2015\\recap\\recap\\MagicTrick\\input\\MagicTrick-1052.in"))