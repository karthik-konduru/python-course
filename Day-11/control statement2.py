#break
nums=[10,20,33,24,57,378]
target=int(input())
for i in range(len(nums)):
    if nums[i]==target:
        print(f"Element found at index: ",i)
        break
else:
    print('Element not found')
#assert
n=10
assert n==10
print(n)
#