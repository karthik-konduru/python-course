n=int(input())
if n>0:
    if n%2==0:
        print('N is positive and even')
    else:
        print('N is positive and Odd')
elif n<0:
    if n%2==0:
        print('N is Negative and even')
    else:
        print('N is Negative and Odd')
else:
    print('Number is Equal to Zero')