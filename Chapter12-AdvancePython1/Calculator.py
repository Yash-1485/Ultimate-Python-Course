#Addition
def addition(*args):
    if len(args)==0:
        return 0
    sum=0
    for x in args:sum+=x
    return sum

#Subtraction
def subtraction(*args):
    if len(args)==0:
        return 0
    sub=0
    for x in args:sub-=x
    return sub

#Multiplication
def multiplication(*args):
    if len(args)==0:
        return 1
    mul=1
    for x in args:mul*=x
    return mul

#Division
def division(*args):
    if len(args)==0:
        return 1
    div=args[0]
    for x in args[1:]:div/=x
    return float('%.4f' %div)

#Modulation
def modulation(*args):
    if len(args)==0:
        return 0
    mod=args[0]
    for x in args[1:]:mod%=x
    return mod

#Power
def power(*args):
    if len(args)==0:
        return 0
    pow=args[0]
    for x in args[1:]:pow**=x
    return pow

if(__name__=='__main__'):print('Hello World!')