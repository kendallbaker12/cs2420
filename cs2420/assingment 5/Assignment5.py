import time

class Student(object):
    def __init__(self, lname, fname, ssn, email, age):
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.email = email
        self.age = age

    def GetLastName(self):
        return self.lname

    def GetFirstName(self):
        return self.fname

    def GetSSN(self):
        return self.ssn

    def GetEmail(self):
        return self.email

    def GetAge(self):
        return self.age
    
    def __eq__(self,rhs):
        return self.ssn == rhs.ssn
    
    def __lt__(self,rhs):
        return self.ssn < rhs.ssn
    
    def __le__(self,rhs):
        return self.ssn <= rhs.ssn
    
    def __ne__(self,rhs):
        return self.ssn != rhs.ssn
    
    def __gt__(self,rhs):
        return self.ssn > rhs.ssn
    
    def __ge__(self,rhs):
        return self.ssn >= rhs.ssn
        
    def __int__(self):
        return int(self.ssn.replace("-",""))
    
def main():
    start = time.time()
    fin = open("InsertNames.txt", "r")
    students = []
    avg = 0
    c = 0
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        repeat = False
        for s2 in students:
            if s2.GetSSN() == s.GetSSN():
                print("Error.", s.GetFirstName(), "is repeat!")
                repeat = True;
                break
        if repeat == False:
            students.append(s)
        
    print(len(students))
    fin.close()
    end = time.time()
    print("time taken to get student objects from InsertNames.txt is:", end - start)
    for i in range(len(students)):    
        s = students[i]
        avg += int(s.GetAge())
        c += 1
        
    if c > 0:
        avg = avg / c
        print("Average age is:", avg)
    
    

    start = time.time()
    fin = open("RetrieveNames.txt")
    avg = 0
    c = 0
    UnfoundStudent = []
    for ssn in fin:
        ssn = ssn.strip()
        found = False
        for i in range(len(students)):
            s1 = students[i]
            if s1.GetSSN() == ssn:
                avg += int(s1.GetAge())
                c += 1
                found = True
        if found == False:
            UnfoundStudent.append(ssn)
    if c > 0:
        avg = avg / c
        print("Average age is:", avg)
    else:
        print("No student has the same ssn")
    if UnfoundStudent:
        print("These {} are the unfound students {}".format(len(UnfoundStudent),UnfoundStudent))
    fin.close()
    end = time.time()
    print("Time taken for RetrieveNames is:", end - start)

    start = time.time()
    fin = open("DeleteNames.txt")
    UndeletedStudent = []
    for ssn in fin:
        ssn = ssn.strip()
        found = False
        for i in range(len(students)):
            s2 = students[i]
            if s2.GetSSN() == ssn:
                found = True
                students.pop(i)
                break
        if found == False:
            UndeletedStudent.append(ssn)
    if UndeletedStudent:
        print("These {} are the undeleted students {}".format(len(UndeletedStudent),UndeletedStudent))
    fin.close()
    end = time.time()
    print("Time taken for DeleteNames is:", end - start)

main()