#Polymorphism
class cal:
    def addition1(self,a,b,c=0,d=0):
        return a+b+c+d
b=cal()
print(b.addition1(20,4))
print(b.addition1(20,30,40))
print(b.addition1(1,2,3,4))