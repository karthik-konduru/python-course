# Fourth Highest Value in a list
l=[-2,-77,74,0,7,18,5,33,12,22]
first=second=third=f=float('-inf')
for num in l:
    if num>first:
        f=third
        third=second
        second=first
        first=num
    elif num>second and num<first:
        f=third
        third=second
        second=num    
    elif num>third and num<second and num<first:
        f=third
        third=num
    elif num>f and num<first and num<second and num<third:
        f=num
print(f)