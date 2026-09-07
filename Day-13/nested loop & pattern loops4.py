#printing serial numbers
n=int(input())
c=1
for i in range(1,n+1):
    for j in range(n):
        print(c,end=' ')
        c+=1
    print()