
import  numpy as np
arr = np.array([1,2,3,4,5])
print (arr)
marks = [10,20,30,40,50,60]
marks_array =np.array(marks)
print(marks_array)
##dimensions
print(arr.ndim)
arr2=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr2.ndim)
# no.of rows and coloums
print(arr.shape)
print(arr2.shape)

## no.of elements
print(arr.size)
print(arr2.size)

print()
print()
## array operators
arr1 = np.array([10,20,30,])
arr2  =np.array([1,2,3])
print(arr1+arr2)
arr3  =np.array([1])#size is different.
print(arr1+arr3)
#all operators
arr1 = np.array([10,20,30,])
arr2  =np.array([1,2,3])
print(arr1-arr2)
print(arr1*arr2)
#array operations using aggregate functions
arr = np.arry([10,20,30,40,50])
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))