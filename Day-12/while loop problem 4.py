l=[-2,-77,74,0,7,18,5,33,12,22]
first=second=float('-inf')
for num in l:
    if num>first:
        second=first
        first=num
    elif num>second and num<first:
        second=num
print(second)