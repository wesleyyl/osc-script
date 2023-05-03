#this file must be within a folder in the osc-script directory
#output runStats.txt file in the evolution directory with batchrun.py & runBatchRun.sh

import sys, os
from pathlib import Path


#rootPath = '/home/wesleyluk/oscillator/evolution'
rootPath = os.path.dirname(os.path.dirname( __file__ ))
savedModels = os.path.join(rootPath, 'evolution/saved_models')

#print(rootPath)
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


filename = "runStats.txt"
#filepath = os.path.join(rootPath, 'osc-scripts', filename)
filepath = os.path.join(rootPath, filename)


if (os.path.exists(filepath)):
    with open(filepath, 'r') as file: 
        data = file.readlines()

    data[1] = str(fileCount + int(data[1])) + "\n"

    with open(filepath, 'w') as file:
        file.writelines(data)
        file.write("\n" + str(fileCount))
else:
    with open(filepath, 'w') as file:
        file.write("Number of Zip Files Generated:\n")
        file.write(str(fileCount) + '\n')
        file.write("\nFile Deletion Log:")
        file.write('\n' + str(fileCount))
