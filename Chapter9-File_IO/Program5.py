# Write a program to mine a log file and find out whether it contains ‘python’.
# Write a program to find out the line number where python is present from ques 6.
with open("Chapter9-File_IO/log.txt") as f:
    # content = f.read()
    c=1
    while (line:=f.readline())!="":
        if 'Python' in line:
            print('Yes, python is available in file at line no.',c)
            break
        c+=1
    else:print('No, python is not available in file')