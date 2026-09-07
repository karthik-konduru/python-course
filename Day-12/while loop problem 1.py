# Finding Maximum element in list
l=[90,56,3,2,15,789,7]
maximum=float('-inf')
for num in l:
    if num>maximum:
        maximum=num
print(maximum)