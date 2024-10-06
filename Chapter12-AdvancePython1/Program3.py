# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

try:
    div=a/b
    print('Division is: ',div)
except ZeroDivisionError as e:
    print('Division is: Infinite')
except Exception as e:
    print(e)
print('Rest of code')