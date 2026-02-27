#InstanceMethodEx1.py
#Program for demonstrating instance method
class Student:
    def readstuddata(self,objinfo):
        #print("ID of current object in method=",id(self))
        print("Enter {} Object information".format(objinfo))
        self.sno=int(input("\t Enter Student Number:"))
        self.name=input("\t Enter Student Name:")
        self.marks=float(input("\t Enter Student Marks:"))
        print("==========================================")
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
print("Content of s1=",s1.__dict__)
print("Content of s2=",s2.__dict__)
#read instance data for s1
#print("ID of  s1 in main program=",id(s1))
s1.readstuddata("First")
#read instance data for s2
#print("ID of  s2 in main program=",id(s2))
s2.readstuddata("Second")
s1.city="HYD"
s2.place="Mujauna"
#After reading print the content
print("================================")
print("Content of s1=",s1.__dict__)
print("Content of s2=",s2.__dict__)
#Display the data of first student
s1.dispstuddata("First")
print("\t Student city=",s1.city)
#Display second student data
s2.dispstuddata("Second")
print("\t Student place=",s2.place)