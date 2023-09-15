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
S1 + S1 -> S0 + S0; k0*S1*S1
S0 + S2 -> S1; k1*S0*S2
S1 -> S1+S2; k2*S1
S2 -> S2+S1; k3*S2
S1 -> S2+S2; k4*S2
S1 -> S2; k5*S1
S1 -> S2; k6*S1
S0 + S0 -> S0; k7*S0*S0
S1 + S0 -> S0; k8*S1*S0
k0 = 0.9761368718849311
k1 = 81.9604780009613
k2 = 7.8204959297189935
k3 = 13.685952708431088
k4 = 20.48363989613687
k5 = 4.82406814562916
k6 = 5.59885139003004
k7 = 6.0961829926489
k8 = 0.5485748150852173
S0 = 1.0
S1 = 5.0
S2 = 9.0
"""


output = analyzeAntimony.countReactions(ant)

print(output)

#r = te.loada(ant)