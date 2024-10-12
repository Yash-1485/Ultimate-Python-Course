# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
try:
    with (open('Chapter12-AdvancePython1/1.txt') as f1, open('Chapter12-AdvancePython1/2.txt') as f2, open('Chapter12-AdvancePython1/3.txt') as f3):
        f1_data=f1.read()
        f2_data=f2.read()
        f3_data=f3.read()
        print(f1_data)
        print(f2_data)
        print(f3_data)
except FileNotFoundError as e:print(e)
except Exception as e:print(e)
print('Rest of code')