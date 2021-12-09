import time


class Student():
    def __init__(self,lname,fname,ssn,email,age):
        self.lname = lname
        self.fname = fname
        self.ssn = ssn
        self.email = email
        self.age = age
        
    def getlastname(self):
        return self.lname
    
    def getfirstname(self):
        return self.fname
    
    def getssn(self):
        return self.ssn
    
    def getemail(self):
        return self.email
    
    def getage(self):
        return self.age
def main():    
    fin = open("InsertNames.txt" , "r")
    students = []
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        repeat = False
        for s2 in students:
            if s2.getssn == s.getssn():
                print(s.getfirstname , "is repeat")
                repeat = True;
            if repeat == False:
                students.append(s)
    
    fin.close()
main()