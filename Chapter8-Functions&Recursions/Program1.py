#Write a program using functions to find greatest of three numbers.
def find_greater(n1,n2,n3):
    if n1>n2 and n1>n3:return n1
    elif n2>n3:return n2
    else:return n3
print(find_greater(10,20,30))
#with parameters with return