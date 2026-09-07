# Finding Third maximum element in list
l=[1,2,3,4,5]
first=second=third=float('-inf')
for num in l:
    if num>first:
        third=second
        second=first
        first=num
print(third)