# Write a program to print the following star pattern: 
# *
# **
# *** for n = 3
n=int(input('Enter: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()