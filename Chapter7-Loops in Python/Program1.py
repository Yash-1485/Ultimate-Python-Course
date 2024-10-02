#Write a program to print multiplication table of a given number using for loop.
n=int(input('Enter a number to print it\'s Multiplication Table: '))
#Using for loop
# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')

#Using while loop
i=1
while (i<=10):
    print(f'{n} x {i} = {n*i}')
    i+=1
