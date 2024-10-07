# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
from random import randint as rn
def game():
    with open("Chapter9-File_IO/Hi-Score.txt") as f:
        hs=f.read()
        if hs=="":hs=0
        else:hs=int(hs)

        ns=rn(1,1000)
        print('New Score is:',ns)
        if ns>hs:
            with open("Chapter9-File_IO/Hi-Score.txt",'w') as file:
                file.write(str(ns))
                print('New Hi-score is:',ns)
        else:print('Hi-score is:',hs)

game()