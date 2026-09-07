d2={'name':'Codegnan','branch':'hyderabad','batch':'PFS66','no_students':51}
print(d2)
d2.update({'key':'value'})
print("printing updated dictionary:",d2)
d2.pop('key')
print("key value is deleted and printing  dictionary:",d2)
d2.popitem()#removes last key and vale
print("last value & key  is deleted while using(popitem())",d2)
print(d2.keys())#it can print keys.
print(d2.values())#it can print values.
print(d2.items())#it can print dictionay as list.
