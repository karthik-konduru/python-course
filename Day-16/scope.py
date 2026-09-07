#local scope
def f():
    x=10 #varible we can access only in side the  function
    print(x)
f()
###print(x)# there will be error (name 'x' is not defined) because variable x is stored in inside the function.

#global scope
z=20 #variable we can acess any where inside the function and outside the function
def f1():
    print(z)
f1()
print (z)#variable also print here.

# enclosing scope

def f3():
    k=40
    print(k)
    def f4():
        a=30
        print(a)
    f4()
f3()
# 4. Build in Function
def f3():
    l=[1,2,3]
    return sum(l)
f3()