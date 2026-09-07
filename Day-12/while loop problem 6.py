l=[-2,-77,74,0,7,18,5,33,12,22]
first=second=third=float('-inf')
for num in l:
    if num>first:
        third=second
        second=first
        first=num
    elif num>second and num<first:
        third=second
        second=num    
    elif num>third and num<second and num<first:
        third=num
print(third)