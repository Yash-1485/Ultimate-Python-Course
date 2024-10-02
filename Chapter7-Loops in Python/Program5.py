#Write a program to calculate the factorial of a given number using for loop.
n=int(input('Enter a number to find it\'s Factorial: '))
fact=1
for i in range(1,n+1):
    fact*=i
print('Factorial of given number is:',fact)