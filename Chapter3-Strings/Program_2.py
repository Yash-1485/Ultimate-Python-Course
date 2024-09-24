letter='''
    Dear <|Name|>,
    You are selected!
    <|Date|>
    '''
name=input("Enter your name: ")
date=input("Enter date: ")

# letter=letter.replace('<|Name|>',name)#returns a string
# letter=letter.replace('<|Date|>',date)
letter=letter.replace('<|Name|>',name).replace('<|Date|>',date)#We can chaining(make a chain) the replace function
print("After changing fields in template:",letter)