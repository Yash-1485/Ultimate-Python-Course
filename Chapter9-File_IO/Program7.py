# Write a program to find out whether a file is identical & matches the content of another file.
file1=input('Enter path of file 1: ')
file2=input('Enter path of file 2: ')

with open(file1) as f1:content1=f1.read()
with open(file2) as f2:content2=f2.read()

if content1==content2:print("Yes")
else:print("No")