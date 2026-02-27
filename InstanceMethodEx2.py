#Program for readinng and displaying instance method data
#InstanceMethodEx2.py
class Student:
    def readstuddata(self,objinfo):
        #print("ID of current object in method=",id(self))
        print("Enter {} Object information".format(objinfo))
        self.sno=int(input("\t Enter Student Number:"))
        self.name=input("\t Enter Student Name:")
        self.marks=float(input("\t Enter Student Marks:"))
        print("==========================================")
        self.dispstuddata(objinfo) #Calling instance method by using self
    def dispstuddata(self,objinfo):
        print("{} Object Information".format(objinfo))
        print("\t Student Number:{}".format(self.sno))
        print("\t Student Name:{}".format(self.name))
        print("\t Student Marks:{}".format(self.marks))
        print("===========================================")
#Main program
#create an object of student
s1=Student()
s2=Student()
#Read s1 data and display
s1.readstuddata("First")
#Read s2 data and display
s2.readstuddata("Second")