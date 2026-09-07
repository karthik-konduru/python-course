# Finding second maximum element in list
l=[1,2,3,4,5]
first=second=float('-inf')
for num in l:
    if num>first:
        second=first
        first=num
print(second)