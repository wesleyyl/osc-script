import sys, os
import tellurium as te

evDir = '/home/wesleyluk/oscillator/evolution/evolution'

sys.path.insert(0, evDir)

os.chdir(evDir)

#print(os.getcwd())

import analyzeAntimony
#import evolUtils as ev

### TEST THAT IT CORRECTLY IDS AUTOCATALYTIC REACTIONS

ant = """
var S0
var S1
var S2
S2 + S2 -> S1; k0*S2*S2
S2 + S1 -> S2; k1*S2*S1
#S1 -> S1+S1; k2*S1
S1 -> S1+S0; k3*S1
S0 -> S2; k4*S0
S1 + S2 -> S0 + S0; k5*S1*S2
S2 + S2 -> S2; k6*S2*S2
k0 = 8.680236126254428
k1 = 26.85692353910657
k2 = 79.60138295777838
k3 = 8.732629841149377
k4 = 14.235117544154281
k5 = 1.888528394353246
k6 = 11.030768229912944
S0 = 1.0
S1 = 5.0
S2 = 9.0
"""


output = analyzeAntimony.countReactions(ant)

print(output)

#r = te.loada(ant)