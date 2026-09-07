#Nested if Conditional Statement
a,b,c=map(int,input().split())
if a==b or a==c:
    print(a)
elif a==b:
    if c>a:
        print(c)
    else:
        print(a)
elif b==c:
    if a>b:
        print(a)
    else:
        print(b)
elif a==c:
    if b>a:
        print(b)
    else:
        print(a)
elif a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
