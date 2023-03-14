#this file must be within a folder in the oscillator folder

import sys, os

rootPath = '/home/wesleyluk/oscillator/evolution'
savedModels = os.path.join(rootPath, 'saved_models')

#print(savedModels)


fileCount = 0

for file in os.listdir(savedModels):
    #print(file[:4])
    #fileCount = 0
    if (file[:4]) == "FAIL":
        try:
            #print(os.path.join(savedModels, file))
            os.remove(os.path.join(savedModels, file))
            print(file + " deleted")
            fileCount+= 1
        except:
            break

print(str(fileCount) + " deleted")
