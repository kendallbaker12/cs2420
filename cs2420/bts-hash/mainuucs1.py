import uucs1
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
    uuc = uucs1.UUC()
    TotalCount = 0
    start = time.time()
    fin = open("InsertNamesMedium.txt", "r")
    avg = 0
    c = 0
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4] )
        if not uuc.Insert(s):
            TotalCount += 1
    print("The total number of repeats.",TotalCount)
    print("the length of the list is ",uuc.Size())
    end = time.time()
    print("Time taken for InsertNames is: ",end - start,"seconds")
    fin.close()

    fin = open("RetrieveNamesMedium.txt", "r")
    start = time.time()
    TotalCount = 0
    for line in fin:
        ssn = line.strip()
        s = Student("","",ssn,"","0")
        s2 = uuc.Retrieve(s)
        if s2 is None:
            TotalCount += 1
        else:
            gTotalAge += int(s2.GetAge())
            TotalCount += 1
    print("Avg Age of retrieved students is",gTotalAge/TotalCount)
    end = time.time()
    print("Time taken for RetrieveNames is: ",end - start,"seconds")
    fin.close()
        
    fin = open("DeleteNamesMedium.txt", "r")
    start = time.time()
    avg = 0
    c = 0
    TotalCount = 0
    for line in fin:
        ssn = line.strip()
        s = Student("","",ssn,"","0")
        if not uuc.Delete(s):
            TotalCount +=1
    print("Total number of deleted items.",TotalCount)
    end = time.time()
    print("Time taken for DeleteNames is: ",end - start,"seconds")
    fin.close()
    
        
    #taverse
    gTotalAge = 0
    uuc.Traverse(AddAges)
    print("The average age is", gTotalAge / uuc.Size() )
    
    
    
main()
