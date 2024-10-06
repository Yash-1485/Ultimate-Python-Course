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