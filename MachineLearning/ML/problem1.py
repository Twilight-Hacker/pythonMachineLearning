import sys

def parseCSVLine(line):
    res = []
    for x in line.split(","):
        res.append(int(x))
    return res


class PerceptronF():
    def __init__(self):
        self.b = 0
        self.w_1 = 0
        self.w_2 = 0
        
    def UpdateWeights(self, mag, data):
        self.b = self.b + mag
        self.w_1 = self.w_1 + mag*data[0]
        self.w_2 = self.w_2 + mag*data[1]
        
    def calc(self, x):
        return self.b + self.w_1*x[0] + self.w_2*x[1]
    
    def output(self):
        return str(self.w_1)+","+str(self.w_2)+","+str(self.b)+"\n"
        

inFN = sys.argv[1]
outFN = sys.argv[2]

data = []
xV = []
yV = []
labelsV = []

with open(inFN) as fIn:
    for line in fIn:
        dl = parseCSVLine(line)
        xV.append(dl[0])
        yV.append(dl[1])
        labelsV.append(dl[2])
        data.append(dl)


fun = PerceptronF()
fOut = open(outFN, 'w')

converged = False

while (not converged):
    converged = True
    for item in data:
        if(item[2]*fun.calc((item[0], item[1])) <= 0):
            fun.UpdateWeights(item[2], (item[0], item[1]))
            converged = False
            fOut.write( fun.output() )
            
            
            

fOut.close()

