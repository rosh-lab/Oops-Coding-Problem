#MethodsNeed.py===
class Student:
    crs="Python" #here crs is called class level data member
#Main program
Student.cnt="India" #here cnt is called class level data member of student
s1=Student()
s2=Student()
#Place Instance data member in s1 object
s1.sno=int(input("Enter first student number:"))
s1.name=input("Enter first student name:")
s1.marks=float(input("Enter first student marks:"))
print("======================================")
#Place Instance data member in s2 object
s2.sno=int(input("Enter ssecond student number:"))
s2.name=input("Enter second student name:")
s2.marks=float(input("Enter second student marks:"))
print("=======================================")
#Display s1 object data(Instance data member)
print("First student number=",s1.sno)
print("First student name=",s1.name)
print("First student marks=",s1.marks)
print("First student course=",s1.crs)
print("First student country=",s1.cnt)
print("=====================================")
#Display s2 object data(Instance data member)
print("Second student number=",s2.sno)
print("Second student name=",s2.name)
print("Second student marks=",s2.marks)
print("Second student course=",s2.crs)
print("Second student country=",s2.cnt)
print("=====================================")

