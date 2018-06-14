#=======================================================================================================================
#=== photosorter - order and sort your photos ==========================================================================
#=======================================================================================================================
#=== Albert Ratajczak ==================================================================================================
#=== Last update: 2018-06-14 ===========================================================================================
#=======================================================================================================================
#=======================================================================================================================

from myfiles import *

inputPath = 'F:/photosorterTEST'
outputPath = 'sorted'

myPhotos = MyFiles(inputPath, outputPath)

myPhotos.dirsTree(fullTree = True)

myPhotos.sortFiles()



