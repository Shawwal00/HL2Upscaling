import os
import sys
import shutil

originalFolderPath = sys.argv[1]
toCopyFolder = sys.argv[2]

for path, folders, files, in os.walk(originalFolderPath):
    for fileName in files:
        if "_normal" in str(fileName):
            print("saffsa")
        else:
            fullPath = os.path.join(str(originalFolderPath), str(path), str(fileName))
            print(fullPath)
            shutil.copy2(fullPath, toCopyFolder)
