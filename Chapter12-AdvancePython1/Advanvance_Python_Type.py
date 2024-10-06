from typing import List
class Employee:
    def __init__(self,name,salary,desg):
        self.name=name
        self.salary=salary
        self.desg=desg
    def getData(self) -> str:
        return f'Name:{self.name}\nDesignation:{self.desg}\nSalary:{self.salary}\n'

class EmployeeManager:
    def __init__(self,employees):
        self.employees:List[Employee]=employees
    
    def getData(self):
        for emp in self.employees:
            print(emp.getData())

emps=[Employee('Yash',10000000,'CEO'),Employee('Hitarth',980000,'CMO'),Employee('Shivrajsinh',1000000,'CTO')]
em=EmployeeManager(emps)
print(em.getData())