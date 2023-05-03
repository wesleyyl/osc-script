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
            return ant.read().decode('utf-8')

def readSeedStr(zipFile):
    with ZipFile(zipFile) as zipF:
        for file in zipF.namelist():
            if (file[:4]) == "seed":
                filename = str(file)

        with zipF.open(filename) as seed:
            seed_str = seed.read().decode('utf-8')
            #print(seed_str)
            return seed_str

def readConfig(zipFile):
    with ZipFile(zipFile) as zipF:
        with zipF.open('config.txt') as cfg:
            return cfg.read().decode('utf-8')

def catalyticweeder(antStr):
    uni_uni = 0
    uni_bi = 0
    bi_uni = 0
    bi_bi = 0
    degrade = 0
    autocatalysis = 0
    total = 0
    lines = antStr.splitlines()
    for line in lines:
        if '->' in line and not line.startswith('#'):
            total += 1
            line = line.replace(' ', '')  # strip spaces
            # separate products and reactants by splitting at ->
            reaction = line.split('->')
            reactants = reaction[0]
            # Remove the rate constant part
            products = reaction[1].split(';')[0]
            rxnType = ''
            # Get reaction type by number of reactants and products
            if '+' in reactants:
                rxnType += 'bi-'
            else:
                rxnType += 'uni-'
            # Now we do the same thing for the product half
            if '+' in products:
                rxnType += 'bi'
            else:
                rxnType += 'uni'

            if rxnType == 'uni-uni':
                uni_uni += 1
            elif rxnType == 'uni-bi':
                uni_bi += 1
                # Separate products (reactants is already just one item
                products = products.split('+')
                if reactants in products:
                    autocatalysis += 1
            elif rxnType == 'bi-uni':
                bi_uni += 1
                # products is already one item, need to split reactants
                reactants = reactants.split('+')
                if products in reactants:
                    degrade += 1
            elif rxnType == 'bi-bi':  # bi-bi
                bi_bi += 1
                # We should have already checked for null reactions, where reactant and product are the same,
                # so we're not going to check for that here.
                # Separate products and reactants
                reactants = reactants.split('+')
                products = products.split('+')
                if (reactants[0] == products[0] and reactants[0] == products[1]) or \
                        (reactants[1] == products[0] and reactants[1] == products[1]):
                    autocatalysis += 1
        else:  # if the line is not a reaction, move to the next line
            continue
    # This dictionary contains the PORTION of each reaction type
    rxnDict = {
        'uni-uni': uni_uni / total,
        'bi-uni': bi_uni / total,
        'uni-bi': uni_bi / total,
        'bi-bi': bi_bi / total,
        'autocatalysis': autocatalysis / total,
        'degradation': degrade / total,
        'total': total
    }

    if rxnDict['autocatalysis'] != 0:
        return True
    else:
        return False

fileList = [i for i in (os.path.join(savedModels, f) for f in os.listdir(savedModels)) if os.path.isfile(i)]

#print(fileList)


for zipFile in fileList:
    filepath = os.path.join(savedModels, zipFile)
    #print(os.path.exists(filepath))

    seedNum = readSeedStr(filepath)

    seed = str(seedNum) + ".txt"
    seedPath = os.path.join(extractedAnt, seed)
    
    # if os.path.exists(seedPath):
    #     continue

    antStr = readAntStr(filepath)
    modelConfig = readConfig(filepath)
    catalytic = catalyticweeder(antStr)

    if catalytic:
        seedPath = os.path.join(extractedAnt, f"Z_AUTOCAT_{seed}")
        newZipPath = os.path.join(savedModels, f"Z_AUTOCAT_{seedNum}.zip")
        os.rename(filepath, newZipPath)

    with open(seedPath, 'w') as file:
        file.write('Seed: ' + str(seedNum)+ '\n*\n\n')
        file.write(antStr)
        file.write('\n*\n')
        file.write(modelConfig)




"""
    with open(seedPath, 'w') as file:        
        if catalytic:
            newFP = os.path.join(savedModels, f"Z_AUTOCAT_{seedNum}.zip")
            os.rename(filepath, newFP)
        file.write('Seed: ' + str(seedNum)+ '\n\n')
        file.write(antStr)
        file.write('\n\n\n')
        file.write(modelConfig)

    if catalytic:
        os.rename(seedPath, f"Z_AUTOCAT_{seed}")
"""
    # with open(seedPath, 'wb') as file:
    #     antStr = readAntStr(filepath)
    #     file.write(('Seed: ' + str(seedNum)+ '\n\n').encode())
    #     file.write(antStr)





""" TO RESTORE THE ORIGINAL STATE
for zipFile in fileList:
    filepath = os.path.join(savedModels, zipFile)
    #print(os.path.exists(filepath))

    seedNum = readSeedStr(filepath)

    seed = str(seedNum) + ".txt"
    seedPath = os.path.join(extractedAnt, seed)
    
    # if os.path.exists(seedPath):
    #     continue

    with open(seedPath, 'w') as file:
        antStr = readAntStr(filepath)
        modelConfig = readConfig(filepath)
        catalytic = catalyticweeder(antStr)
        #if catalytic:
            #newFP = os.path.join(savedModels, f"Z_AUTOCAT_{seedNum}.zip")
        os.rename(filepath, os.path.join(savedModels, f"{seedNum}.zip"))
        file.write('Seed: ' + str(seedNum)+ '\n\n')
        file.write(antStr)
        file.write('\n\n\n')
        file.write(modelConfig)

    # if catalytic:
    #     os.rename(seedPath, f"Z_AUTOCAT_{seed}")

"""