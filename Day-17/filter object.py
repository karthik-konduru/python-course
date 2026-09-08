# Filter()
numbers=[1,2,3,4,5,6]
res=filter(lambda x: str(x), numbers)
print(res)
numbers=[1,2,3,4,5,6]
res=filter(lambda x: str(x), numbers)
print(res)
print(list(res))
numbers=[1,2,3,4,5,6]
res=filter(lambda x: x%2==0, numbers)
print(res)
print(list(res))