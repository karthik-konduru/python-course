# By using Explicit then we can access the values in results as tuple
t=(1,2,3)
l=list(t)
print(t)
print(l)
l[0]=10
print(l)
t1=tuple(l)
print(t1)

# tuple bult-in functions.
print(t1.count(10))
print(t1.index(3))