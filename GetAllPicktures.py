import os
import sys
originalFolderPath = sys.argv[1]
print (originalFolderPath)
for path, folders, files, in os.walk(originalFolderPath):
    for fileName in files:
        if str(fileName).endswith(".jpg"):
            print(str(fileName))
