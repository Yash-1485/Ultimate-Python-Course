#Using loop - Method1
marks=[]
for i in range(6):
    mark=float(input(f'Enter marks for student #{i+1}: '))
    marks.append(mark)
marks.sort()
print(marks)

#Using Loop - Method 2
# marks=[i for i in list(input(f'Enter marks for student: ').strip().split())]
# marks=[float(i) for i in input(f'Enter marks for student: ').strip().split()]
# marks=[int(i) for i in list(input(f'Enter marks for student: ').strip().split())]
# marks.sort()
# print(marks)

#Using eval
# marks=eval(input('Enter marks: '))
# marks.sort()
# print(marks)