#Program for calculating factorial of a given number by using classes and objects..
#OopsFactorialEx2.py
class Fact:
    def getval(self):
        while(True):
            try:
                self.n=int(input("Enter a number for Cal Factorial:"))
            except ValueError:
                print("Invalid input-----try again")
            else:
                break
    def calFact(self):
        if(self.n<0):
            return("For -ve number there is no factorial")
        else:
            fact=1
            for i in range(1,self.n+1):
                fact=fact*i
            return fact
    def dispresult(self):
        self.getval()
        print("Factorial ({})==>{}".format(self.n,self.calFact()))
#Main program
Fact().dispresult() #Nameless object calling...
