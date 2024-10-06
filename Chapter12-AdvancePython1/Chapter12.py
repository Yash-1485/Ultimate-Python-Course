from typing import Tuple
# using walrus operator
# if (n:=len((1,2,3,4,5)))>3:
#     print('Lenght of list is greater than 3 and it is:',n)

# if (l:=(1,2,3,4,5))==(1,2,3,4,5):
#     print(l)

#Types in Python
# def list_num(n:int) -> list:
#     return list(i for i in range(1,n+1))
# ll=list_num(10)
# print(ll)

#Advance Types
# number:int=1
# print(number)

# mylist:Tuple[str,int]=('Hello World!',2,3,4)
# print(mylist)

#Match Case
# while True:
#     n=int(input('Enter your choice: '))
#     match n:
#         case 1:print('You\'ve choosed case 1')
#         case 2:print('You\'ve choosed case 2')
#         case 3:print('You\'ve choosed case 3')
#         case 4:print('You\'ve choosed case 4')
#         case 5:print('You\'ve choosed case 5')
#         case _:
#             print('Valid cases are from 1 to 5')
#             break

#Dictonary merged and update operators
# dict1={'Name':'Yash','RollNo':3}
# dict2={'Subject':'Python','Marks':100}
# print(dict1)
# print(dict2)
# merged=dict1|dict2
# print(dict1)
# print(dict2)
# dict1.update(dict2)
# print(merged)
# print(dict1)

#Exception Handling
# a=10
# b=0
# try:
#     div=a/b
#     print(div)
# except Exception as e:
#     print(e)
# print('Rest of code')

# while True:
#     try:
#         n=int(input('Enter a number: '))        
#     except Exception as e:
#         print('Kindly enter digits only')
#     else:
#         print(n)
#         break

#Multiple Try and Except Blocks and Exception raising
# while True:
#     try:
#         n=int(input('Enter even digits only: '))
#         try:
#             if n%2!=0:
#                 raise Exception('Enter even digits only')
#         except Exception as e:
#             print(e)
#         else:
#             print('Number is okay')
#             break
#     except ValueError as e:
#         print('Except-Block-1')
#         print(e)
#     except Exception as e:
#         print('Except-Block-2')
#         print(e)

#Using Try-Except block with finally with original use of finally block
# def myFunc():
#     try:
#         n=int(input('Enter numbers only: '))
#         return n
#     except Exception as e:return e
#     finally:print('Bye Bye!')
#     print('Hello World!')
# print(myFunc())

#Use of global keyword
# class Test:
#     a=10
#     @staticmethod
#     def myFunc():
#         global a
#         a=11
#         # return a
#         print(a)
# Test.myFunc()

#List Comprehension and Enumrate function in python
# list=list(i for i in range(11,21))
# # print(list)
# enumerate
# for i,item in enumerate(list,0):
#     print('index-',i,' | ','item-',item)
n=5
for x in range(1,n+1):
    print('*'*x)

for x in range(1,n+1):
    print('*'*n)

for x in range(n,0,-1):
    print('*'*x)