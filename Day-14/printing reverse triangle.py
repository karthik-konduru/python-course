n=int(input())
for r in range(n):
    #spaces
    for c in range(r):
        print(' ',end=' ')
    #stars
    for c in range(2*n-(2*r+1)):
        print('*',end=' ')
    print()
        