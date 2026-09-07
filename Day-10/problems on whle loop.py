# Counting the number if digits in a given number
n=int(input())
c=0
while n>0:
    c+=1
    n//=10
print(c)
# problem 2
# Reversing numbers of a given number
n=int(input())
rev=0
while n>0:
    rem=n%10
    n//=10
    rev=rev*10+rem
print(rev)
#problem3
# Sum of digits in a given number
n=int(input())
total=0
while n>0:
    rem=n%10
    total+=rem
    n//=10
print(total)
#problem4
n=input()
total=0
for ch in n:
    total+=int(ch)
print(total)
#problem5
n=int(input())
total=0
string=str(n)
for ch in string:
    total+=int(ch)
print(total)
#problem6
string=input()
res=''
for ch in string:
    res+=ch.upper()
print(res)
#problem7
name='karthik'
for ch in name:
    print(ch)
