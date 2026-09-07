#printing croos symbol.
n=int(input())
for r in range(n):
    for c in range(n):
        if r==c or (r+c)==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()