import sys
import numpy as np

def parseCSVLine(line):
    res = []
    for x in line.split(","):
        res.append(float(x))
    return res

class RegrFun():
    def __init__(self, alpha):
        self.rate = alpha
        self.b_0 = 0
        self.b_age = 0
        self.b_weight = 0
        self.iter = 0
        
    def getIterations(self):
        return self.iter
    
    def iterate(self):
        self.iter = self.iter + 1
    
    def getAlpha(self):
        return self.rate
        
    def getB0(self):
        return self.b_0
    
    def getBAge(self):
        return self.b_age
    
    def getBWeight(self):
        return self.b_weight
    
    def setB0(self, val):
        self.b_0 = val
        
    def setBAge(self, val):
        self.b_age = val
        
    def setBWeight(self, val):
        self.b_weight = val
    
        
        

inFN = sys.argv[1]
outFN = sys.argv[2]

data = []
age = []
weight = []
heightL = []

with open(inFN) as fIn:
    for line in fIn:
        dl = parseCSVLine(line)
        datapoint = [1, dl[0], dl[1]]
        heightL.append(dl[2])
        age.append(dl[0])
        weight.append(dl[1])
        data.append(datapoint)


ageAvg = np.mean(age)
ageSigma = np.std(age)
weightAvg = np.mean(weight)
weightSigma = np.std(weight)


for line in range(len(data)): 
    data[line][1] = (data[line][1]-ageAvg)/ageSigma
    data[line][2] = (data[line][2]-weightAvg)/weightSigma

fOut = open(outFN, 'w')
rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]

for a in rates:
    regFun = RegrFun(a)
    for i in range(100):
        for line in range(len(data)):
            temp1 = regFun.getB0() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])
            temp2 = regFun.getBAge() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])*data[line][1]
            temp3 = regFun.getBWeight() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])*data[line][2]
            regFun.setB0(temp1)
            regFun.setBAge(temp2)
            regFun.setBWeight(temp3)
        regFun.iterate()
    rep = str(regFun.getAlpha()) + "," + str(regFun.getIterations()) + "," + str( regFun.getB0() ) + "," + str( regFun.getBAge() ) + "," + str( regFun.getBWeight() ) + "\n"
    fOut.write(rep)


regFun = RegrFun(0.03)
for i in xrange(120):
    for line in range(len(data)):
        temp1 = regFun.getB0() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])
        temp2 = regFun.getBAge() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])*data[line][1]
        temp3 = regFun.getBWeight() - (regFun.getAlpha()/len(data))*(regFun.getB0() + regFun.getBAge()*data[line][1] + regFun.getBWeight()*data[line][2] - heightL[line])*data[line][2]
        regFun.setB0(temp1)
        regFun.setBAge(temp2)
        regFun.setBWeight(temp3)
    regFun.iterate()

rep = str(regFun.getAlpha()) + "," + str(regFun.getIterations()) + "," + str( regFun.getB0() ) + "," + str( regFun.getBAge() ) + "," + str( regFun.getBWeight() ) + "\n"
fOut.write(rep)        


fOut.close()

