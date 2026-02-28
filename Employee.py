#Employee.py===>>File name and module name
class Employee:
    def readempdata(self):
        print("*"*50)
        self.eno=int(input("\t Enter Employee Number:"))
        self.ename=input("\t Enter Employee Name:")
        self.sal=float(input("\t Enter Employee Salary:"))
