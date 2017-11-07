from UnitTester import UnitTester
from UnitTestable.Postman import postman
from UnitTestable.SixSidedDie import sixsideddie
'''
Import Unit Tester and Import Testing Program
'''
#inputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheet
# s\\Solutions_Div2_Problemset1\\recap\\Cameras\\input"
#outputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Cameras\\output"
ut = UnitTester()
#ut.test_is_same_as_output(inputFolder, outputFolder, cameras)


#inputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Gravity\\input"
#outputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Gravity\\output"
#ut.test_is_same_as_output(inputFolder, outputFolder, gravity)


# inputFolder = "C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\Postman\\input"
# outputFolder = "C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\Postman\\output"
# ut.test_is_same_as_output(inputFolder, outputFolder, postman)


inputFolder = "C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\SixSides\\input\\"
outputFolder = "C:\\Users\\Tyler\\OneDrive\\Documents\\Github\\ACM\\UnitTests\\SixSides\\output"
ut.test_is_same_as_output(inputFolder, outputFolder, sixsideddie)