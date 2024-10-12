# Store the multiplication tables generated in problem 3 in a file named Tables.txt.
n=int(input('Enter a number: '))

with open('Chapter12-AdvancePython1/Tables.txt','w') as f:
    for i in range(1,n+1):
        for j in range(1,11):
            f.write(f'{i} x {j} = {i*j}\n')
        else:
            f.write('------------------\n')