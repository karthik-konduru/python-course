# Finding that number is prime number or not
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print('Prime Number')
else:
    print('Not Prime Number')