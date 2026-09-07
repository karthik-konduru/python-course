#Set Operations.
s1={10,20,30,40}
s2={45,55,10,5}
print("printing s1 union s2:",s1.union(s2))
print(s1 | s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
print(s1.symmetric_difference(s2))
print(s1^s2)
#Frozen Set
s=frozenset([10,20,30])
print(s)
s1={12,2,4,6}
s2={4,6}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))