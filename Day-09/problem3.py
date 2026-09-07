a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print('All are Equal')
elif a==b or b==c:
    print('Two Numbers are Equal')
elif a>b and a>c:
    print(f'{a} is greater')
    print('a is greater')
elif b>a and b>c:
    print(f'{b} is greater')
    print('b is greater')
else:
    print(f'{c} is greater')