# Write a program to make a copy of a text file “this. txt”
with open("Chapter9-File_IO/this.txt") as f:
    content=f.read()

with open("Chapter9-File_IO/thisCopy.txt","w") as f:
    f.write(content)