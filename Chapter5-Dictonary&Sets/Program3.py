# st={18,'18'}
# print(st)

# st=set()
# st.add(20)
# st.add(20.0)
# st.add('20')
# print(st,'->',len(st))

# st=set()
# print(type(st))
# dt={}
# print(type(dt))

favlang={}
for i in range(4): 
    name=input('Enter friends name: ')
    lang=input('Enter your favourite language: ')
    favlang.update({name:lang})
print(favlang)