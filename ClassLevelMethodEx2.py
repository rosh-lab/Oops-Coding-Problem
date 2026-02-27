#program for demonstrating Class level method
#ClassLevelMethodEx2.py
class Student:
    @classmethod
    def getcrses(cls):
        cls.crs="Python" #here crs is called class level data member
        cls.geturname()#Calling class level method w.r.t cls
        #Student.geturname()===>>We can also call by class name
    @classmethod
    def geturname(cls):
        cls.urname="JNTU-HYD" #Here urname is called class level data member



#main program
Student.getcrses() #Calling class level method by using class name
#Student.geturname() ===>>Here also we get an answer
print("Courses=",Student.crs)
print("Student University=",Student.urname)
print("=====OR==============================")
s1=Student()
s1.getcrses() #calling class level method by using object name
print("Couses=",s1.crs)
print("Student University=",s1.urname)