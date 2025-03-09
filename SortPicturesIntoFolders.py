import os
import sys
import shutil
from pathlib import Path

originalFolderPath = sys.argv[1]
thisFolderPath = sys.argv[2]
outputFolderPath = sys.argv[3]

materials = str("materials")
startChecking = False

for originalPath, originalFolders, originalFiles, in os.walk(originalFolderPath):
    for originalFileName in originalFiles:
        splitPath = Path(str(originalPath)).parts
        startChecking = False
        fullFolderPath = None 
        for folders in splitPath:
            if str(folders) == materials:
                startChecking = True
                newOutputFolderPath = os.path.join(str(outputFolderPath), materials)
                fullPathMinusMaterials = os.path.join(str(outputFolderPath))
                if not os.path.exists(newOutputFolderPath):
                        os.makedirs(newOutputFolderPath)
            if startChecking == True:
                fullFolderPath = str(folders)
                fullPath = os.path.join(str(fullPathMinusMaterials), str(fullFolderPath))
                fullPathMinusMaterials = fullPath
                if not os.path.exists(fullPath):
                    os.makedirs(fullPath)
                    for path, folders, files, in os.walk(thisFolderPath):
                        for fileName in files:
                            print(originalFileName)
                            if str(Path(fileName).stem) == str(Path(originalFileName).stem):
                                fullVTFPath = os.path.join(str(path), str(fileName))
                                shutil.copy2(fullVTFPath, fullPath)


##for path, folders, files, in os.walk(thisFolderPath):
##   for fileName in files:
##        for originalPath, originalFolders, originalFiles, in os.walk(originalFolderPath):
##            for originalFileName in originalFiles:
##               if str(Path(fileName).stem) in str(Path(originalFileName).stem):
##                     fullPath = os.path.join(str(thisFolderPath), str(path), str(fileName))
##                     shutil.copy2(fullPath, outputFolderPath)



