# Write a program to filter a list of numbers which are divisible by 5.
ls=[i for i in range(1,101)]
newList=list(filter(lambda x:x%5==0,ls))
print(newList)