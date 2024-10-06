# Write a program to print third, fifth and seventh element from a list using enumerate function.
ls=[i for i in range(1,11)]
for index,item in enumerate(ls,1):
    if(index==3 or index==5 or index==7):print(f'{index} - {item}')