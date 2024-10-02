#Write a recursive function to calculate the sum of first n natural numbers.
# def sum_of_numbers(n,sum=0):
#     if(n==0):
#         print('Sum is:',sum)
#         return
#     sum+=n
#     sum_of_numbers(n-1,sum)
# sum_of_numbers(10)

# def sum_of_numbers(n):
#     if (n==0):
#         return 0
#     return n+sum_of_numbers(n-1)
# print(sum_of_numbers(10))

# add=0
# def sum_of_numbers(n):
#     if (n==0):
#         return globals()['add']
#     globals()['add']+=n
#     return sum_of_numbers(n-1)
# print(sum_of_numbers(10))