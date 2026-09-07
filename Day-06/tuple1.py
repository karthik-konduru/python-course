#basic tuple program.
t=()
t1=tuple()
t=(1,2,1,2,1,3,4,5)
print(t[5])
# t[5]=6
# print(t)
t=(1,2,3,[10,20,30])
print(len(t))
t[3][2]=300
print(t)
print(len(t))