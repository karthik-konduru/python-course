#problems.
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()
#
n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print(i,end=' ')
        i+=1
    print()