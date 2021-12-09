class Node:
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

        
class UUC:
    def __init__(self):
        self.mRoot = None
        self.mSize = 0
        
    def Insert(self, item): # returns False if item was a duplicate
        if self.Exists(item):
            return False
        n = Node(item)
        self.mRoot = self.InsertR(n,self.mRoot)
        self.mSize += 1
        return True

    def InsertR(self,n,current):
        if current == None:
            current = n
        elif n.mItem < current.mItem:
            current.mL = self.InsertR(n,current.mL)
        else:
            current.mR = self.InsertR(n,current.mR)
        return current
        
    def Delete(self, item): # returns False if item can't be found
        if not self.Exists(item):
            return False
        self.DeleteR(item,self.mRoot)
        self.mSize -= 1
        return True

    def DeleteR(self,item,current):
        if item < current.mItem:
            current.mL = self.DeleteR(item,current.mL)
        elif item > current.mItem:
            current.mR = self.DeleteR(item,current.mR)
        else:
            if current.mL is None and current.mR is not None:
                current = current.mR
            elif current.mL is not None and current.mR is None:
                current = current.mL
            elif current.mL is None and current.mR is None:
                current = None
            else:
                successor = current.mR
                while successor.mL is not None:
                    successor = successor.mL
                current.mItem = successor.mItem
                current.mR = self.DeleteR(successor.mItem,current.mR)
        return current

    def Retrieve(self,item):
        return self.RetrieveR(item,self.mRoot)
    
    
    def RetrieveR(self, item,current): # returns the whole student, or None
        while current != None:
            if current.mItem == item: #if current item is item
                return current.mItem # return current item
            elif current.mItem > item: # if current item is greater than item
                return self.RetrieveR(item,current.mL) #return left current
            else:
                return self.RetrieveR(item,current.mR) #recursive
        return None

    def Exists(self, item):
        return self.ExistsR(item,self.mRoot)

    def ExistsR(self,item,current):
        if current == None:
            return False
        elif current.mItem == item:
            return True
        elif item < current.mItem:
            return self.ExistsR(item,current.mL)
        else:
            return self.ExistsR(item,current.mR)
    #def Size(self):
        count = 0
        count[0]=0
        self.SizeR(count,self.mRoot)
        return count[0]

    #def SizeR(self,count,current):
        if current != None:
            count[0] += 1
            self.SizeR(count,current.mL)
            self.SizeR(count,current.mR)
    def Size(self):
        return self.mSize
    

    def Traverse(self, callbackFunction):
        self.TraverseR(callbackFunction,self.mRoot)
    
    def TraverseR(self,callbackFunction,current):
        if current is None:
            return
        callbackFunction(current.mItem)
        self.TraverseR(callbackFunction,current.mL)
        self.TraverseR(callbackFunction,current.mR)