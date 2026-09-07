n=int(input())
for i in range(n):
    #spaces
    for j in range(n-i):
        print(' ',end=' ')
    #Stars
    for j in range(2*i+1):
        print('*',end=' ')
    print()