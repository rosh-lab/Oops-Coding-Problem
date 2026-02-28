#Teacher.py===>>>File name and module name
class Teacher:
    def readteacherdata(self):
        print("*" * 50)
        self.tno=int(input("\t Enter Teacher Number:"))
        self.tname=input("\t Enter Teacher Name:")
        self.subject=input("\t Enter Teacher Subject:")
        self.exp=float(input("\t Enter Teacher Experience:"))