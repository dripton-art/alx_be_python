import math

class Shape:
     def area(self):
        raise NotImplementedError("Subclasses must implement the area method.") 

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        Area = self.length * self.width
        return Area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        Area = math.pi * self.radius**2
        return Area

