import math

# Base class
class Polygon:
    def area(self):
        pass


# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Square class
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Regular Pentagon class
class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))


# Testing the program
rect = Rectangle(10, 5)
square = Square(4)
triangle = Triangle(6, 3)
pentagon = Pentagon(5)

print("Rectangle Area:", rect.area())
print("Square Area:", square.area())
print("Triangle Area:", triangle.area())
print("Pentagon Area:", round(pentagon.area(), 2))