# Write a program to wipe out the content of a file using python.
file=input('Enter path of file: ')

with open(file,"w") as f:f.write("")