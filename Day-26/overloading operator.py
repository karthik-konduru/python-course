
#Operator Overloading
print(10+20)
print('Python' + 'Code')
print([1,2,4] + [6,7,8])

############ example
class calc:
    def __init__(self,val):
        self.val=val
    def __add__(self,another):
        return self.val+another.val
a=calc(10)
b=calc(100)
c=calc(200)
res=(a+b)+c.val
print(res)