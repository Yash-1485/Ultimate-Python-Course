dictonary={
    'Billi':'Cat',
    'Kutta':'Dog',
    'Chidiya':'Sparrow',
    'Madad':'Help',
    'Kursi':'Chair'
}

word=input('Enter a word to search through hindi dictonary: ')
if word in dictonary:
    print(dictonary[word])
else:
    print('Given word doesn\'t exists.')