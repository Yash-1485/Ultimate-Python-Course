#Reading Data from file
# f=open('Chapter9-File_IO/newFile.txt')
# data=f.read()
# print(data)
# f.close()

#Reding data from file line by line
# f=open('Chapter9-File_IO/newFile.txt')
# # lines=f.readlines()
# # print(lines,type(lines))
# while (line:=f.readline())!="":
#     print(line,type(line))
# f.close()

#Writing Data into file
# f=open('Chapter9-File_IO/file.txt','w')
# f.write('Hello World!\n')
# f.write('1234567890')
# f.close()

#Use of with keyword - no need to close file
with open("Chapter9-File_IO/newFile.txt") as file:
    print(file.read())