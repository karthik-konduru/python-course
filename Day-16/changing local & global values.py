#changing global value.
x=20
def f2():
    global x #(using global keyword for changing global value)
    x=x+10
f2()
print(x)

#changing local value.
def outer():
    x=10
    def inner():
        nonlocal x  #(using nonlocal keyword for chaning local value)
        x=x+100
        print(x)
    inner()
outer()