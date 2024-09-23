class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,city):
        self.name=name
        self.salary=salary
        self.city=city
    def getInfo(self):
        print("Name:",self.name,"\nCompany:",self.company,"\nCity:",self.city,"\nSalary:",self.salary)
yash=Programmer("Yash",13000000,"Ahmedabad")
hitarth=Programmer("Hitarth",1200000,"Surendranagar")
yash.getInfo()
print("-----------")
hitarth.getInfo()