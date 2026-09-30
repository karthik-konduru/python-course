from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        area=self.side*self.side
        return area
    def perimeter(self):
        p=4*self.side
        return p
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
square=Square(4)
rectangle=Rectangle(10,5)
print(square.area())
print(square.perimeter())
print(rectangle.area())
print(rectangle.perimeter())