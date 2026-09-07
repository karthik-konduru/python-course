#problems.
#FizzBuzz
number=int(input())
if number%3==0 and number%5==0:
    print('FizzBuzz')
elif number%3==0:
    print('Fizz')
elif number%5==0:
    print('Buzz')
else:
    print(f'{number} is Wrong Input Valid Number')

# Greatest Between Two Numbers
n1=int(input())
n2=int(input())
if n1>n2:
    print(f'{n1} is greater than {n2}')
else:
    print(f'{n2} is greater than {n1}')

# Greatest Between Among 3 numbers
a,b,c=map(int,input().split())
if a==b and b==c:
    print('All are Equal')
elif a==b or b==c or a==c :
    print('Two Numbers are Equal')
elif a>b and a>c :
    print(f'{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater than {a} and {c}')
else:
    print(f'{c} is greater than {a} and {b}')
