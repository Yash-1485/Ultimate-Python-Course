# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
# n=1
# with open(f'Chapter9-File_IO/Tables/Table{n}.txt','w') as file:
#     for i in range(1,10):
#         file.write(f'{n} x {i} = {n*i}\n')
#     else:file.write(f'{n} x {i+1} = {n*(i+1)}')

n=2

while n<=20:
    with open(f'Chapter9-File_IO/Tables/Table{n}.txt','w') as file:
        for i in range(1,10):
            file.write(f'{n} x {i} = {n*i}\n')
        else:file.write(f'{n} x {i+1} = {n*(i+1)}')
    n+=1