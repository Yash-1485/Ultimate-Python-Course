from functools import reduce as r
# Write a program to find the maximum of the numbers in a list using the reduce function.
ls=[1,4,7,2,8,90,23,45,67,12,89,56,100,342,51,4,6,2,89,0,1]
myFunc=lambda x,y:x if x>y else y
# print(type(myFunc))
print(r(myFunc,ls))
# print(list(set(ls)))-->Unique values in list