#basic nested loop
M=[[1,2,3],[4,5,6],[7,8,9]]
for row in range(len(M)):
    for column in range(len(M)):
        print(M[row][column],end =' ')