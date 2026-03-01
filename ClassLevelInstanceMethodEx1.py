#classLevelInstanceMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="Python"
        cls.geturname()
    @classmethod
    def geturname(cls):
        cls.urname="JNTU-HYD"
    def readstuddata(self,objinfo):
        #print("ID of current object in method=",id(self))
        print("Enter {} Object information".format(objinfo))
        self.sno=int(input("\t Enter Student Number:"))
        self.name=input("\t Enter Student Name:")
        self.marks=float(input("\t Enter Student Marks:"))
        print("==========================================")
    def dispstuddata(self,objinfo):
        self.getcrs() #Calling class level method w.r.t class or self name from instance method
        print("{} Object Information".format(objinfo))
        print("\t Student Number:{}".format(self.sno))
        print("\t Student Name:{}".format(self.name))
        print("\t Student Marks:{}".format(self.marks))
        print("\t Student University:{}".format(self.urname))
        print("\t Student course:{}".format(self.crs))
        print("===========================================")
#main program
#Student.getcrs()===>>>Calling through class name
s1=Student()
s2=Student()
#s1.getcrs() #Calling through object name
print(s1.__dict__)
print(s2.__dict__)
s1.readstuddata("First")
s2.readstuddata("Second")
s1.dispstuddata("First")
s2.dispstuddata("Second")
print(s1.__dict__)
print(s2.__dict__)