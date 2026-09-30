#Method Overloading
class cal:
    def addition1(self,*a):
        return sum(a)
b=cal()
print(b.addition1(20,4))
print(b.addition1(20,30,40))
print(b.addition1(1,2,3,4))
print(b.addition1(1,2,3,4,5,6,7,8,9,10))
print()