class Student:
    def __init__(self,sno,name,marks):
        self.sno=sno
        self.name=name
        self.marks=marks
s1=Student(50,"Arshad",23.2)
s2=Student(30,"Roshan",21.2)
s3=Student(20,"Ramsha",87.2)
print(s1.sno,s1.name,s1.marks)
print(s2.sno,s2.name,s2.marks)
print(s3.sno,s3.name,s3.marks)