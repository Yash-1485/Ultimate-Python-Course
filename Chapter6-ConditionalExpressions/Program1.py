#Write a program to find the greatest of four numbers entered by the user.
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
d=int(input('Enter fourth number: '))

if a>b and a>c and a>d:print(f'a = {a} is greater number')
elif b>c and b>d:print(f'b = {b} is greater number')
elif c>d:print(f'c = {c} is greater number')
else:print(f'd = {d} is geater number')