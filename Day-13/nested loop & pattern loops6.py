#printing odd & even number.
n=int(input())
even=2
odd=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(even,end=' ')
            even+=2
        else:
            print(odd,end=' ')
            odd+=1
    print()