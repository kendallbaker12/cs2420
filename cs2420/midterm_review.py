def exists(self,item):
    return self.existsR(item,self.mRoot)

def existsR(self,item,current):
    if current is None:
        return False
    elif current.mItem = item:
        return True
    elif item < current.mItem:
        return self.existsR(item,current.mL)
    else:
        return self.existsR(item,current.mR)

def existsR(self,item,current):
    if current is None:
        return False
    elif current.mItem = item:
        return True
    elif item < current.mItem:
        return self.existsR(item,current.mL)
    else:
        return self.existsR(item,current.mR)

def size(self):
    count = 0
    count[0] = 0
    self.sizeR(count,self.mRoot)
    return count[0]

def sizeR(self,count,current):
    if current != None:
        count[0] += 1
        self.sizeR(count,current.mL)
        self.sizeR(count,current.mR)
        
