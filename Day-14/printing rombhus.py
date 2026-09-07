n=int(input())
for i in range(n):
    #spaces
    for j in range(n-1-i):
        print(' ',end=' ')
    #Stars
    for j in range(2*i+1):
        print('*',end=' ')
    print()
for r in range(n):
    #spaces
    for c in range(r):
        print(' ',end=' ')
    #stars
    for c in range(2*n-(2*r+1)):
        print('*',end=' ')
    print()