'''
Created on 24 Ìבס 2017

@author: Galadar
'''

class dataSet():
    def __init__(self, first):
        self.Datalist = []
        self.dim = len(first)
        self.Datalist.append(first)
        self.ColNames = [" "]*self.dim
        
    def addItem(self, item):
        if(len(item)!=self.dim):
            raise Exception("Data missing in item")
            return
        else:
            self.Datalist.append(item)
            
    def DataList(self):
        return self.Datalist
    
    def Rank(self):
        return self.dim
    
    def Size(self):
        return len(self.Datalist)
    
    def RetrieveItem(self, pos):
        return self.Datalist[pos]
    
    def SetColName(self, col, name):
        if(col<0) | (col>=self.dim):
            raise Exception("IndexOutOfBounds")
            return
        self.ColNames[col] = name
    
    def GetColName(self, col):
        if(col<0) | (col>=self.dim):
            raise Exception("IndexOutOfBounds")
            return
        if(self.ColNames[col]==" "):
            return "NA"
        else:
            return self.ColNames[col]
    
    def RetrieveColNames(self):
        return self.ColNames
    
    def GetDataPoint(self, ind=0, col=0):
        if(ind<0) | (ind>=self.Size()):
            raise Exception("IndexOutOfBounds")
            return
        if(col<0) | (col>=self.Rank()):
            raise Exception("IndexOutOfBounds")
            return
        if(self.Datalist[ind][col]==" ") | (self.Datalist[ind][col]=="") | (self.Datalist[ind][col]==None):
            return "NA"
        else:
            return self.Datalist[ind][col]
        
    def First(self):
        return self.Datalist[0]
    
    def Last(self):
        return self.Datalist[self.Size()-1]

