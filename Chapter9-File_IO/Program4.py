# Hey Donkey, how can you that?
# You donkey you are such a bad guy
# No donkey is donkey as you are

# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("Chapter9-File_IO/GoodWords.txt") as file:
    lines=file.readlines()

    with open("Chapter9-File_IO\GoodWords.txt",'w') as wr:
        for line in lines:
            wr.write(line.replace('Donkey','######'))