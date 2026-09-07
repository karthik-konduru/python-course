# sets.
s = set()
s1 = {}
print(type(s), type(s1))
print(s,s1)
s.add(10)
print("element 10 is added to set(S):",s)
s.update([20,30,40])
print("set is updated :",s)
s.remove(20)
print("removing element 20 from set:",s) 

s.discard(300)# if element wii have it will remove other wise it will ignore. it does not show error.
print("discard method:if element wii have it will remove other wise it will ignore. it does not show error.")
print (s)
print(s.pop())#removes element.
s.clear()#remove values in the set.
print(s)
del s1 #delete est permently
