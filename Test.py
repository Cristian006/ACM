from UnitTester import UnitTester
from UnitTestable.Cameras import cameras
from UnitTestable.Gravity import gravity
from UnitTestable.Islands import islands

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


inputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Islands\\input"
outputFolder = "C:\\Users\\Tyler\\Google Drive\\AlgorithmsCheatSheets\\Solutions_Div2_Problemset1\\recap\\Islands\\output"
ut.test_is_same_as_output(inputFolder, outputFolder, islands)
