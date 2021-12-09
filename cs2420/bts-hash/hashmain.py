import hash
from traverse_delete_retrieve import Student
import time

def PrintNames(item):
    print(item)
    
def PrintEarlyNames(item):
    if item < "M":
        print(item)

gTotalAge = 0
def AddAges(item): # assuming items are students
    global gTotalAge
    gTotalAge += int(item.GetAge())
    
def main():
    global gTotalAge
    uuc = hash.UUC(300000)
    TotalCount = 0
    start = time.time()
    fin = open("InsertNamesMedium.txt", "r")
    avg = 0
    c = 0
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4] )
        if not uuc.Insert(s):
            TotalCount +=1
    print(TotalCount)
    print(uuc.Size())
    fin.close()
    
    gTotalAge = 0
    uuc.Traverse(AddAges)
    print("The average age is", gTotalAge / uuc.Size() )

        
    fin = open("DeleteNamesMedium.txt", "r")
    avg = 0
    c = 0
    TotalCount = 0
    for line in fin:
        ssn = line.strip()
        s = Student("","",ssn,"","0")
        if not uuc.Delete(s):
            TotalCount +=1
    print(TotalCount)
    fin.close()
    
    fin = open("RetrieveNamesMedium.txt", "r")
    gTotalAge = 0
    TotalCount = 0
    ErrorCount = 0
    for line in fin:
        ssn = line.strip()
        s = Student("","",ssn,"","0")
        s2 = uuc.Retrieve(s)
        if s2 is None:
            ErrorCount += 1
        else:
            gTotalAge += int(s2.GetAge())
            TotalCount += 1
    print("Avg Age of retrieved students is",gTotalAge/TotalCount)
    print(ErrorCount)
    fin.close()
    
        
    

    
    
    
main()