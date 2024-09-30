#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
marks=[]
for i in range(3):
    marks.append(float(input(f'Enter marks of subject #{i+1}: ')))
per=sum(marks)/3
if per>=40 and marks[0]>=33 and marks[1]>=33 and marks[2]>=33:print('Pass')
# elif per>=40 and marks[0]<=33 or marks[1]<=33 or marks[2]<=33:
else:print('Fail')