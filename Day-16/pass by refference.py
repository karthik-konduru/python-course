#pass by value.
def f (x):
    print(id(x))
    print(x)
a= 20
print(id(a))
f(a)

#pass by object refference.
def f (x):
    x=[10,20,30]
    print(id(x))
    print(x)
a=[40,50]
print(id(a))
f(a)


## Pass by Object reference using immutable data type
def f(x):
    x=20
    print(id(x))
    print(x)
a=10
print(id(a))
f(a)


# Pass by Object reference using immutable data type - modification or reassign
def f(x):
    x.append(10)
    print(id(x))
    x=[10,20,30,40]
    print(id(x))
    print(x)
a=[1,2,3,4]
print(id(a))
f(a)