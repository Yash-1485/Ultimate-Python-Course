# Write a python function to remove a given word from a list and strip it at the same 
# time.
ls=['Parekh','Yash','Arun','Pooja','Ila','Hitarth']
# ls=["Harry", "Rohan", "Shubham", "an"]
def rem(list,word):
    new_list=[]
    for item in list:
        if item!=word:
            new_list.append(item.strip(word))
    return new_list

# print(rem(ls,'h'))