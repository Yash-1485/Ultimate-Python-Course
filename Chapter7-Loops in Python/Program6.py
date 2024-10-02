# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
n=int(input('Enter: '))

for i in range(1,n*2,2):
    for k in range(n,i-1,-2):
        print(end=' ')
    for j in range(1,i+1):
        print('*',end='')
    print()