import os
import sys
import shutil
from pathlib import Path

originalFolderPath = sys.argv[1]
thisFolderPath = sys.argv[2]
outputFolderPath = sys.argv[3]
normalFolder = sys.argv[4]

materials = str("materials")
startChecking = False

for originalPath, originalFolders, originalFiles, in os.walk(originalFolderPath):
    for originalFileName in originalFiles:
        splitPath = Path(str(originalPath)).parts
        startChecking = False
        fullFolderPath = None 
        baseTexturePath = None
        rootbaseTexture = None
        for folders in splitPath:
            if str(folders) == materials:
                startChecking = True
                newOutputFolderPath = os.path.join(str(outputFolderPath), materials)
                fullPathMinusMaterials = os.path.join(str(outputFolderPath))
                if not os.path.exists(newOutputFolderPath):
                        os.makedirs(newOutputFolderPath)
            if startChecking == True:
                if baseTexturePath == None:
                    baseTexturePath = 1
                elif baseTexturePath == 1:
                    baseTexturePath = '"' + str(folders).capitalize()
                    rootbaseTexture = baseTexturePath
                else:  
                    baseTexturePath = baseTexturePath + "/" + str(folders)
                    rootbaseTexture = baseTexturePath
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
                                        baseTexturePath = rootbaseTexture + "/" + str(Path(fileName).stem)
                                        correctVMT = open(fileName, "w")
                                        if "decals" in baseTexturePath or "Decals" in baseTexturePath:
                                           correctVMT.write( """"VertexLitGeneric"
{
	"$basetexture" """+ baseTexturePath + '"' + """ 
	"$decal" 1

	"$decalscale" 0.25
}""")

                                        elif "Models" in baseTexturePath:
                                            done = False
                                            for pathNormal, foldersNormal, filesNormal, in os.walk(normalFolder):
                                                for fileNameNormal in filesNormal:
                                                    if (str(fileNameNormal).startswith(Path(fileName).stem)):
                                                        done = True
                                            if done == True:
                                                correctVMT.write(""" "VertexLitGeneric"
                                                         
{
	// Original shader: VertexLitTexture

	"$basetexture" """+ baseTexturePath +'"' + """
	"$bumpmap" """+ baseTexturePath + '_normal' + '"' + """
}
""")
                                            else:
                                                correctVMT.write(""" "VertexLitGeneric"
                                                         
{
	// Original shader: VertexLitTexture

	"$basetexture" """+ baseTexturePath +'"' + """
}
""")
                                        else:
                                            done = False
                                            for pathNormal, foldersNormal, filesNormal, in os.walk(normalFolder):
                                                for fileNameNormal in filesNormal:
                                                    if (str(fileNameNormal).startswith(Path(fileName).stem)):
                                                        done = True
                                            if done == True:
                                                correctVMT.write(""" "LightmappedGeneric"
                                                         
{
	// Original shader: BaseTimesLightmap
	"$basetexture" """+ baseTexturePath + '"' + """
    "$bumpmap" """+ baseTexturePath + '_normal' + '"' + """

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
                                            else:
                                                correctVMT.write(""" "LightmappedGeneric"
                                                         
{
	// Original shader: BaseTimesLightmap
	"$basetexture" """+ baseTexturePath + '"' + """

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
                    for path, folders, files, in os.walk(normalFolder):
                        for originalFileName in originalFiles:
                            for fileName in files:
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



