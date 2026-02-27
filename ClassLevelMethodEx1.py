#program for demonstrating Class level method
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrses(cls):
        cls.crs="Python"
        Student.urname="JNTU" #here crs and urname are called class level data members
        return cls.crs,cls.urname

#main program
Student.getcrses() #Calling class level method by using class name
print("Courses=",Student.crs)
print("Student University=",Student.urname)
print("=====OR==============================")
s1=Student()
s1.getcrses() #calling class level method by using object name
print("Couses=",s1.crs)
print("Student University=",s1.urname)
print("=====OR===============================")
Student().getcrses() #calling class level method by using nameless object
print("Couses=",Student().getcrses()[0])
print("Student University=",Student().getcrses()[1])

