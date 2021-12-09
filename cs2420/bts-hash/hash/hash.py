import math

def IsPrime(x):
    s= int(math.sqrt(x))
    for i in range(2,s+1):
        if x%i==0:
            return False
    return True

class UUC:
    def __init__(self,neededSize):
        actualSize = 2*neededSize+1
        while not IsPrime(actualSize):
            actualSize += 2
        self.mTable = []
        for i in range(actualSize):
            self.mTable.append(None)

        self.mSize = 0
    def Insert(self,item):
        if self.Exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while self.mTable[index]:
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
        self.mTable[index] = item
        self.mSize += 1
        return True
    
    def Delete(self,item):
        if not self.Exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while not (self.mTable[index] and self.mTable[index] == item):
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)                
        self.mTable[index] = False
        self.mSize -= 1
        return True  
    def Retrieve(self,item):
        if not self.Exists(item):
            return None
        key = int(item)
        index = key % len(self.mTable)
        while not (self.mTable[index] and self.mTable[index]== item):
            index += 1
            if index >= len(self.mTable):
                index -= len(self.mTable)
        return self.mTable[index]       

    def Exists(self,item):
        key = int(item)
        index = key % len(self.mTable)
        while True:
            if self.mTable[index] is None:
                return False
            if self.mTable[index] and self.mTable[index] == item:
                return True
            index +=1
            if index >= len(self.mTable):
                index -= len(self.mTable)
    def size(self):

    def Traverse(self,callbackFunction):


