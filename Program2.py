list=[f'{7} x {i} = {7*i}' for i in range(1,11)]
func=lambda x:f'{x}\n'
mystr='\n'.join(list)
print(mystr)