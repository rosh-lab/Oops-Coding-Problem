#ClassLevelDataMemberEx3.py
class Student:
    crs="Python"
    cnt="India"
s1=Student()
s2=Student()
Student.crs="JAVA"
print(s1.crs,s1.cnt)
print(s2.crs,s2.cnt)