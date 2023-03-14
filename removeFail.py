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


filename = "runStats.txt"

if (os.path.exists(filename)):
    with open(filename, 'r') as file: 
        data = file.readlines()

    data[1] = str(fileCount + int(data[1])) + "\n"

    with open(filename, 'w') as file:
        file.writelines(data)
        file.write("\n" + str(fileCount))
else:
    with open(filename, 'w') as file:
        file.write("Number of Zip Files Generated:\n")
        file.write(str(fileCount) + '\n')
        file.write("\nFile Deletion Log:")
        file.write('\n' + str(fileCount))
