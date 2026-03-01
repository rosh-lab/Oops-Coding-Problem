#Program for calculating factorial of a given number by using classes and objects..
#OopsFactorialEx1.py
class Fact:
    def getval(self):
        self.n=int(input("Enter a number for Cal Factorial:"))
    def calFact(self):
        if(self.n<0):
            return("For -ve number there is no factorial")
        else:
            fact=1
            for i in range(1,self.n+1):
                fact=fact*i
            return fact
    def dispresult(self):
        print("Factorial ({})==>{}".format(self.n,self.calFact()))
#Main program
fo=Fact()
fo.getval()
fo.calFact()
fo.dispresult()
