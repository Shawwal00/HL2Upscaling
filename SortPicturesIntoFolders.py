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
                        for originalFileName in originalFiles:
                            for fileName in files:
                                if str(Path(fileName).stem) == str(Path(originalFileName).stem):
                                    if str(fileName).endswith("vmt"):
                                        correctVMT = open(fileName, "w")
                                        correctVMT.write(""" "LightmappedGeneric"
{
	// Original shader: BaseTimesLightmap
	"$basetexture" """+'"'+str(fullFolderPath).capitalize() + "/" + str(Path(fileName).stem)+'"'+ """

	"$texscale"	4
	"$baseTextureOffset" "[0.5 0.5]"
	"Proxies"
     	{
	"TextureTransform"
            {
		"translateVar" "$baseTextureOffset"
		"scaleVar"     "$texscale"
		"resultVar"    "$baseTextureTransform"
            }
     	}
}
""")
                                        correctVMT.close()
                                        fullVMTPath = os.path.abspath(correctVMT.name)
                                        shutil.copy2(fullVMTPath, fullPath)
                                        os.remove(fullVMTPath)
                                    else:
                                        fullVTFPath = os.path.join(str(path), str(fileName))
                                        shutil.copy2(fullVTFPath, fullPath)


##for path, folders, files, in os.walk(thisFolderPath):
##   for fileName in files:
##        for originalPath, originalFolders, originalFiles, in os.walk(originalFolderPath):
##            for originalFileName in originalFiles:
##               if str(Path(fileName).stem) in str(Path(originalFileName).stem):
##                     fullPath = os.path.join(str(thisFolderPath), str(path), str(fileName))
##                     shutil.copy2(fullPath, outputFolderPath)



