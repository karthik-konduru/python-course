#Method Overriding
class A:
    def m1(self):
        print('Parent m1')
class B(A):
    def m1(self):
        print('child m1')
        super().m1()
c=B()
c.m1()
A.m1(c)