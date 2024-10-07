# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
file=open('Chapter9-File_IO/poems.txt')
content=file.read()
if ('Twinkle' or 'twinkle') in content:
    print('It contains \'twinkle\' word')
else:print('It does not contains \'twinkle\' word')

file.close()