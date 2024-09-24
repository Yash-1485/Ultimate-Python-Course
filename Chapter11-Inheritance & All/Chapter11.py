from multipledispatch import dispatch
#Single Inheritance
# class Parent:
#     a=10
#     # name=""
#     def __init__(self,name="Parent"):
#         self.name=name
#         print(f"This is {self.name} class constructor.")
#     def displaya(self):
#         print(f"This is display method of {self.name} class and value of attribute a is {self.a}")
        
# class Child(Parent):
#     a=20
#     b=30
#     name="Child"
#     def __init__(self,name="Child"):
#         super().__init__()
#         self.name=name
#         print(f"This is {self.name} class constructor.")
#     def displaya(self):
#         super().displaya()
#         print(f"This is display method of {self.name} class and value of attribute a is {self.a}")
#     def displayb(self):
#         print(f"This is display method of {self.name} class and value of attribute b is {self.b}")

# p=Parent()
# p.displaya()
# print(type(p))
# c=Child()
# c.displaya()
# c.displayb()
# print(type(c))
# # c=Parent()
# # c.displaya()

#Multilevel Inheritance
# class Parent:
#     a=10
#     def __init__(self,name="Parent"):
#         self.name=name
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of a is:",self.a)
# class Child(Parent):
#     b=20
#     def __init__(self,name="Child"):
#         super().__init__()
#         self.name=name        
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of b is:",self.b)
# class GrandChild(Child):
#     c=30
#     def __init__(self,name="GrandChild"):
#         super().__init__()
#         self.name=name
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of c is:",self.c)
# p=Parent()
# c=Child()
# gc=GrandChild()
# print(p.a)
# print(c.a,c.b)
# print(gc.a,gc.b,gc.c)

#Multiple Inheritance
# class Parent1:
#     a=10
#     def __init__(self,name="Parent1"):
#         self.name=name
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of a is:",self.a)
# class Parent2:
#     a=20
#     def __init__(self,name="Parent2"):
#         self.name=name
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of a is:",self.a)
# class Child(Parent1,Parent2):
#     b=20
#     def __init__(self,name="Child"):
#         super().__init__()
#         self.name=name        
#         print(f"This is a {self.name} class.")
#     def display(self):
#         print("The value of b is:",self.b)
# # p1=Parent1()
# # p2=Parent2()
# c=Child()
# print(c.a,c.b)

#class methods
# a=200
# class Test:
#     a=10
#     def __init__(self,a):
#         self.a=a
#     @classmethod
#     def show(self):
#         print(f"The value of class attribute a is {self.a}")
#         # print(a)
# t=Test(100)
# t.show()
# print(f"The value of instance attribute a is {t.a}")

#Property decoraters and getters and setters
#Example 1
# class Test:
#     @property
#     def name(self):
#         return self.ename
    
#     @name.setter
#     def name(self,value):
#         self.ename=value
# t=Test()
# t.name="Yash Parekh"
# print(t.name)
# print(t.ename)

#Example 2
# class Employee:
#     # ename=""
#     # companyName=""
#     # salary=""
    
#     @property #Decorator
#     def getName(self):#getter for ename
#         return self.ename
    
#     @getName.setter#setter for ename
#     def setName(self,name):
#         self.ename=name

#     @getName.deleter#deleter for ename
#     def deleteName(self):
#         del self.ename
# emp=Employee()
# emp.setName="Yash Parekh"
# print(emp.getName)#Getter
# print(emp.ename)#Attribute
# # del emp.deleteName
# # del emp.ename
# # print(emp.ename)

#Example 3 - With Constructor Overloading
class Student:
    @dispatch()
    def __init__(self):
        pass

    @dispatch(str,str,int)
    def __init__(self,name,course,marks):#*args
        self.name=name
        self.course=course
        self.marks=marks

    @property
    def getName(self):
        return self.name
    @getName.setter
    def setName(self,name):
        self.name=name

    @property
    def getCourse(self):
        return self.course
    @getCourse.setter
    def setCourse(self,course):
        self.course=course

    @property
    def getMarks(self):
        return self.marks
    @getMarks.setter
    def setMarks(self,marks):
        self.marks=marks

# student=Student("Yash","CE",100)
# print(student.getName,student.getCourse,student.getMarks)
# student.setName="Mohan"
# print(student.getName,student.getCourse,student.getMarks)

# st=Student()
# st.setName="Yash Parekh"
# st.setCourse=""
# st.setMarks=0
# print(st.name)
# print(st.getName,st.getCourse,st.getMarks)