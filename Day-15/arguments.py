#positional arguments
def addition4(a,b):
    print(a,b)
    return a+b
print(addition4(10,20))
#keyword arguments
def addition5(a,b):
    print(a,b)
    return(a+b)
c=45
d=55
print(addition5(b=c,a=d))
#default arguments
def addition6(a,b,c=0,d=0):
    print(a,b,c,d)
    return(a+b+c+d)
print(addition6(20,30,10))
#variable length arguments
def addition7(*var):
    print(type(var))
    return sum(var)
print(addition7(10,20,30))
#variable length keyword argument
def addition8(**var):
    print(type(var))
    total = 0 
    for num in var.values():
        total += num
    return total
print(addition8(a=1,b=2,c=3))