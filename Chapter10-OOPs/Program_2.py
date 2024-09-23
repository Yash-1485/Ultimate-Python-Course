import math as m
class Calculator:
    def __init__(self,n):
        self.n=n
    @staticmethod
    def greetuser(name):
        print("Hello,",name)    
    @staticmethod
    def find_square(n):
        return n**2
    @staticmethod
    def find_cube(n):
        return n**3
    @staticmethod
    def find_square_root(n):
        # return m.sqrt(n) (or)
        return n**(1/2)

n=int(input("Enter a number: "))
calc=Calculator(n)
calc.greetuser("Yash")
print("Square of given number is:",calc.find_square(n))
print("Cube of given number is:",calc.find_cube(n))
print("Square Root of given number is:",calc.find_square_root(n))