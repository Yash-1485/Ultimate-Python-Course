class Test:
    a=None
    # def __init__(self,n):
    #     self.a=n

obj=Test()
print("Instance object a value before change is:",obj.a)
obj.a=0
print("Instance object a value after change is:",obj.a)
print("Class Attribute a value is:",Test.a)

# a=None
# print(a)
# a=1
# print(a)