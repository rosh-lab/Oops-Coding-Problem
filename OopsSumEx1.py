#Write a python program which will add two numbers by using classes and objects..
#OopsSumEx1.py===
class Sum:pass

#MAin program
s=Sum()
#print(s.__dict__)
s.a=float(input("Enter First Value:"))
s.b=float(input("Enter Second Value:"))
s.c=s.a+s.b
print("Sum({},{})-->{}".format(s.a,s.b,s.c))
#Rather then writing this print in main program we should go for writing it under class.
