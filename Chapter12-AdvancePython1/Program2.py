#  Write a list comprehension to print a list which contains the multiplication table of a user entered number.
n=int(input('Enter a number: '))

ls=[f'{n} x {i} = {n*i}' for i in range(1,11)]

for i,x in enumerate(ls,1):
    print(f'{i}.)',x)