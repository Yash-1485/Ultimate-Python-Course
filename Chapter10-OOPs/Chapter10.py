#Object oriented programming
class Employee:
    name=""
    language="Python" #Class attributes
    salary=1300000

    #Constructor
    def __init__(self,name):
        self.name=name
        print(self.name,"is a good boy.")

    def getinfo(self):
        print(self.name,self.language,self.salary)

    def setinfo(employee,name,salary,language):
        # employee.name="Yash"
        employee.salary=1000000
        employee.language="JavaScript"
    
    @staticmethod
    def greet():
        print("Good Morning")

emp1=Employee("Yash")
# emp1.name="Yash"#Instance attributes(Object attributes)
# emp1.language="Python"
# print(emp1.language,emp1.salary)
emp1.setinfo("Yash",1300000,"JavaScript")
# Employee.getinfo(emp1)#Just like emp1.getinfo()
emp1.greet()
emp1.getinfo()