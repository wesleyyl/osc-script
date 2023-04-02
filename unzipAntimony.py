import os
import zipfile
from zipfile import *


rootPath = os.path.dirname(os.path.dirname(os.path.abspath( __file__ )))
savedModels = os.path.join(rootPath, 'evolution/saved_models')
extractedAnt = os.path.join(savedModels, 'extracted_ant')

#print(os.path.abspath( __file__ ))

#print(rootPath)

if not os.path.exists(extractedAnt):
    os.makedirs(extractedAnt)
    #print("doesn't exist")

def readAntStr(zipFile):
    with ZipFile(zipFile) as zipF:
        with zipF.open('best_antimony.ant') as ant:
            return ant.read()

def readSeedStr(zipFile):
    with ZipFile(zipFile) as zipF:
        for file in zipF.namelist():
            if (file[:4]) == "seed":
                filename = str(file)

        with zipF.open(filename) as seed:
            seed_str = seed.read().decode('utf-8')
            #print(seed_str)
            return seed_str


fileList = [i for i in (os.path.join(savedModels, f) for f in os.listdir(savedModels)) if os.path.isfile(i)]

#print(fileList)

for zipFile in fileList:
    filepath = os.path.join(savedModels, zipFile)
    #print(os.path.exists(filepath))

    seed = str(readSeedStr(filepath)) + ".txt"
    seedPath = os.path.join(extractedAnt, seed)
    
    with open(seedPath, 'wb') as file:
        antStr = readAntStr(filepath)
        file.write(antStr)

