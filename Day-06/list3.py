#list methods.
l=[1,2,3,4,5,6,6,7]
print(l)
l.append(10)
print(l)
l.append([20,30])
print(l)
print()
print()
print()
l.extend([40,50,60])
print(l)
print()
l.insert(2,[70,80])
print(l)
l.insert(0,0)
print(l)
print()
print(l.pop())#removing last element.
print(l.pop(5))#removing particular index value.
print()
l=[0, 1, [70, 80], 2, [70, 80], [70, 80], 3, 4, 5, 6, 6, 7, 10, [20, 30], 40, 50]
l.remove(6)#removes first element '6'in the list.
print(l)
l.clear() #total list will be clear.
print("list bult-in functions" )
lst=[70,20,90,30,100,50]
print(len(lst))
print(min(lst))
print(max(lst))
print(sum(lst))
lst.sort()
print(lst)
print(sorted(lst))
lst.sort(reverse=True)
print(lst)
print("copying the list into a variable (r)")
r=lst.copy()
print("r=",r)