import os
import sys
import shutil

originalFolderPath = sys.argv[1]
toCopyFolder = sys.argv[2]
normalFolder = sys.argv[3]

allStrings = ["cable", "composite", "console", "customcubemaps", "debug", "effects", "environment maps", "gamepadui", "hlmv", "matsys_regressiontest", "particle", "perftest", "scripted", "shadertest", "sun", "tools", "vgui", "voice", "sprites"]

for path, folders, files, in os.walk(originalFolderPath):
    for fileName in files:
        if "_normal" in str(fileName):
            print("saffsa")
            fullPath = os.path.join(str(originalFolderPath), str(path), str(fileName))
            shutil.copy2(fullPath, normalFolder)
        else:
            do = False
            for string in allStrings:
                if string in str(path):
                    do = True
                    break
            if do == False:
                fullPath = os.path.join(str(originalFolderPath), str(path), str(fileName))
                shutil.copy2(fullPath, toCopyFolder)
