#program for demonstrating the need of static method..
from Employee import Employee
from Teacher import Teacher
from Student import Student
class Hyd:
    @staticmethod
    def dispobjinfo(obj,objinfo):
        #print("I am from static method")
        print(obj.__dict__,type(obj),type(obj.__dict__))
        print("*" * 50)
        print("{} Information".format(objinfo))
        print("*"*50)
        for k,v in obj.__dict__.items():
            print("\t {}----{}".format(k,v))
        print("*"*50)
#Main program
#L1=list() Pre defined builtins module present in every where by default
eo=Employee()
so=Student()
to=Teacher()
#Read the data for different objects
eo.readempdata()
so.readstudata()
to.readteacherdata()
#Display the data of different objects of different classes
#By using single method called static method..
Hyd.dispobjinfo(eo,"Employee") #calling static method by using class name
Hyd.dispobjinfo(so,"Student") ##calling static method by using class name
Hyd.dispobjinfo(to,"Teacher") #calling static method by using class name

