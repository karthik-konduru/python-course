#List comprehension with if else
l=[1,2,3,4,5,6,7,8,9]
r=['even' if x%2==0 else 'odd' for x in l]
print(r)