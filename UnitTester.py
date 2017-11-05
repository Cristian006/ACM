import unittest
import os
'''
Generic Unit Test module to test all acm code
'''
class UnitTester(object):
    def test_is_same_as_output(self,inputFolder, outputFolder, func):
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.inputFilePaths = []
        self.outputFilePaths = []

        """Is program output successfully determined to be the same as given output?"""
        for filename in os.listdir(self.inputFolder):
            if filename.endswith(".in"):
                self.inputFilePaths.append(os.path.join(self.inputFolder, filename))
        for filename in os.listdir(self.outputFolder):
            if filename.endswith(".out"):
                self.outputFilePaths.append(os.path.join(self.outputFolder, filename))

        incorrectOnes = []

        for i in range(len(self.inputFilePaths)):
            inputFilePath = self.inputFilePaths[i]
            outputFilePath = self.outputFilePaths[i]

            output = str(func(inputFilePath)).strip()
            file = open(outputFilePath, 'r')
            validOutputString = ''
            line = file.readline()
            while line:
                validOutputString += line
                line = file.readline()

            validOutputString = validOutputString.strip()

            if validOutputString != output:
                incorrectOnes.append(inputFilePath)
                print(validOutputString + ' == ' + output)
                print( "\n\nOutput: ", validOutputString == output)
            else:
                print("\n\nValid: ", validOutputString == output)

        print("\n\nAmount Wrong: ", len(incorrectOnes))
        print(incorrectOnes)

if __name__ == '__main__':
    unittest.main()