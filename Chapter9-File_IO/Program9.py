# Write a python program to rename a file to “renamed_by_ python.txt.
import os
file=input('Enter path of file: ')
name=input('Enter another name of file: ')
with open(file) as f:
    content=f.read()
os.remove(file)
with open(f'Chapter9-File_IO/{name}.txt',"w") as fcopy:
    fcopy.write(content)