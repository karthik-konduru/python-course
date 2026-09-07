m=[[10,20,20,40],[50,60,70,80],[90,100,200,300],[400,500,600,700]]
d1,d2=0,0
for i in range(len(m)):
    for j in range(len(m[0])):
        if i==j:
            d1+=m[i][j]
        elif (i+j)==(len(m)-1):
            d2+=m[i][j]
print(d1,d2)
print(abs(d1-d2))