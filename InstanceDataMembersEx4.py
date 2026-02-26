#InstanceDataMembersEx4.py
class Student:
    crs="python"
    cnt="Inida"
    def __init__(self,sno,name,marks):
        self.sno=sno
        self.name=name
        self.marks=marks
s1=Student(12,"Arisha",1.23)
s2=Student(20,"Zrisha",3.45)
print("First Student")
print(s1.sno,s1.name,s1.marks,s1.crs,s1.cnt)
print("Second Student")
print(s2.sno,s2.name,s2.marks,s2.crs,s2.cnt)