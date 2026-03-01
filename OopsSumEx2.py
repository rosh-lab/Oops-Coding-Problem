#Program for adding of two numbers by using classes and objects...
#OopsSumEx2.py
class Sum:
    def getvals(self):
        self.a=float(input("Enter First Value:"))
        self.b=float(input("Enter Second Value:"))
    def addvals(self):
        self.c=self.a+self.b
    def dispvals(self):
        print("Sum({},{})-->{}".format(self.a,self.b,self.c))
#Main program
s=Sum()
s.getvals()
s.addvals()
s.dispvals()