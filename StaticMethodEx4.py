#StaticMethodEx4.py
class Employee:
    def readempdata(self):
        print("*"*50)
        self.eno=int(input("\t Enter Employee Number:"))
        self.ename=input("\t Enter Employee Name:")
        self.sal=float(input("\t Enter Employee Salary:"))
class Student:
    def readstudata(self):
        print("*" * 50)
        self.esno=int(input("\t Enter Student Number:"))
        self.sname=input("\t Enter Student Name:")
class Teacher:
    def readteacherdata(self):
        print("*" * 50)
        self.tno=int(input("\t Enter Teacher Number:"))
        self.tname=input("\t Enter Teacher Name:")
        self.subject=input("\t Enter Teacher Subject:")
        self.exp=float(input("\t Enter Teacher Experience:"))
class Hyd:
    @staticmethod
    def dispobjinfo(obj,objinfo):
        #print("I am from static method")
        #print(obj.__dict__,type(obj),type(obj.__dict__))
        print("*" * 50)
        print("{} Information".format(objinfo))
        print("*"*50)
        for k,v in obj.__dict__.items():
            print("\t {}----{}".format(k,v))
        print("*"*50)


#Main program
eo=Employee()
so=Student()
to=Teacher()
#Read the data for different objects
eo.readempdata()
so.readstudata()
to.readteacherdata()
#Display the data of different objects of different classes
#By using single method called static method..
Hyd().dispobjinfo(eo,"Employee") #calling static method by using nameless object
Hyd().dispobjinfo(so,"Student") ##calling static method by using nameless object
Hyd().dispobjinfo(to,"Teacher") #calling static method by using nameless object