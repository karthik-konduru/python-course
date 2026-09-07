# 1. 'with return with parameters'
print("with return with parameters")
def addition(a,b):
    return a+b
sum=(addition(10,20))
print(sum)
#2.with return without parameters
print("with return without parameters")
def addition1():
    a=30
    b=30
    return a+b
print (addition1())
#3.without return with parameters
print("without return with parameters")
def addition2(a,b):
    print(a+b)
addition2(10,20)
#4.without return without parameters
print("without return without parameters")
def addition3():
    a=30
    b=30
    print(a+b)
addition3()
#5.divison using if
def division(a,b):
    if b==0:
        print("division with zero can't divide")
    else:
        return a//b
print(division(10,0))
