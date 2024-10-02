# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

#without parameter without return
def pattern_1():
    n=int(input('Enter the number: '))
    for i in range(1,n+1):
        print("*"*(n-i+1))
pattern_1()