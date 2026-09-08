# reduce()
from functools import reduce
numbers=[1,2,3,4,5]
res=reduce(lambda a,b: a+b,numbers)
print(res)