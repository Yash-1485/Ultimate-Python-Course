#Write a program to find whether a given number is prime or not.
n=int(input('Enter a number to find it\'s prime or not: '))

if n<=1:print('Not Prime Number')
else:
    ans=True
    i=2
    while(i<n):
        if(n%i==0):
            ans=False
            break
        i+=1
    if ans:print('Prime Number')
    else:print('Not Prime Number')