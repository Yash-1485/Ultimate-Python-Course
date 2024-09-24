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